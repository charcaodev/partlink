import json
import uuid
import random
from datetime import datetime, timedelta
from decimal import Decimal

from faker import Faker

fake = Faker()


class SyntheticDatasetGenerator:

    def __init__(self):

        self.data = {
            "roles": [],
            "customers": [],
            "users": [],
            "sites": [],
            "parts": [],
            "inventory": [],
            "assets": [],
            "work_orders": [],
            "work_order_assignments": [],
            "work_order_parts": [],
            "component_failures": [],
            "asset_component_history": [],
            "part_refurbishments": []
        }

        self.generate_all()

    # -------------------------------------------------
    # HELPERS
    # -------------------------------------------------

    def uuid(self):
        return str(uuid.uuid4())

    def random_past_date(self, days=365):

        return (
            datetime.utcnow() -
            timedelta(
                days=random.randint(1, days),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59)
            )
        ).isoformat()

    # -------------------------------------------------
    # ROLES
    # -------------------------------------------------

    def generate_roles(self):

        roles = [
            "admin",
            "technician",
            "planner",
            "inventory_manager",
            "field_engineer"
        ]

        for role in roles:

            self.data["roles"].append({
                "id": self.uuid(),
                "name": role
            })

    # -------------------------------------------------
    # CUSTOMERS
    # -------------------------------------------------

    def generate_customers(self):

        customers = [
            "Delta Airlines",
            "Alaska Airlines",
            "United Airlines",
            "American Airlines",
            "Southwest Airlines"
        ]

        for customer in customers:

            self.data["customers"].append({
                "id": self.uuid(),
                "name": customer,
                "industry": "aviation",
                "sla_tier": random.randint(1, 3)
            })

    # -------------------------------------------------
    # USERS
    # -------------------------------------------------

    def generate_users(self, users_per_customer=10):

        role_ids = [r["id"] for r in self.data["roles"]]

        for customer in self.data["customers"]:

            for _ in range(users_per_customer):

                self.data["users"].append({
                    "id": self.uuid(),
                    "customer_id": customer["id"],
                    "role_id": random.choice(role_ids),
                    "email": fake.unique.email(),
                    "first_name": fake.first_name(),
                    "last_name": fake.last_name(),
                    "is_active": 1,
                    "created_at": self.random_past_date(900)
                })

    # -------------------------------------------------
    # SITES
    # -------------------------------------------------

    def generate_sites(self):

        AIRLINE_HUBS = {

            "Delta Airlines": [
                ("Atlanta", "GA"),
                ("Detroit", "MI"),
                ("Minneapolis", "MN")
            ],

            "Alaska Airlines": [
                ("Seattle", "WA"),
                ("Portland", "OR")
            ],

            "United Airlines": [
                ("Chicago", "IL"),
                ("Denver", "CO"),
                ("Houston", "TX")
            ],

            "American Airlines": [
                ("Dallas", "TX"),
                ("Charlotte", "NC"),
                ("Phoenix", "AZ")
            ],

            "Southwest Airlines": [
                ("Dallas", "TX"),
                ("Las Vegas", "NV"),
                ("Denver", "CO")
            ]
        }

        for customer in self.data["customers"]:

            hubs = AIRLINE_HUBS.get(customer["name"], [])

            for city, state in hubs:

                self.data["sites"].append({
                    "id": self.uuid(),
                    "customer_id": customer["id"],
                    "name": f"{city} Maintenance Hub",
                    "city": city,
                    "state": state,
                    "country": "USA"
                })

    # -------------------------------------------------
    # PARTS
    # -------------------------------------------------

    def generate_parts(self):

        PART_CATALOG = [

            ("Hydraulic Pump", "critical"),
            ("Fuel Nozzle", "high"),
            ("Brake Assembly", "critical"),
            ("Turbofan Blade", "critical"),
            ("Navigation Computer", "high"),
            ("Pressure Valve", "medium"),
            ("Landing Gear Actuator", "critical"),
            ("Cabin Pressure Sensor", "medium"),
            ("Oil Filter", "low"),
            ("Avionics Control Unit", "high"),
            ("Cooling Fan", "medium"),
            ("Ignition Module", "high"),
            ("Hydraulic Seal", "medium"),
            ("Engine Bearing", "critical"),
            ("Fuel Pump", "high")
        ]

        for i, (part_name, criticality) in enumerate(PART_CATALOG):

            self.data["parts"].append({
                "id": self.uuid(),
                "part_number": f"AV-{100000 + i}",
                "description": part_name,
                "unit_cost": round(random.uniform(500, 50000), 2),
                "criticality": criticality,
                "lead_time_days": random.randint(2, 180)
            })

    # -------------------------------------------------
    # INVENTORY
    # -------------------------------------------------

    def generate_inventory(self):

        warehouses = [
            "SEA Parts Depot",
            "ATL Maintenance Storage",
            "ORD Inventory Center",
            "DFW Logistics Hub",
            "DEN Aircraft Supply",
            "PHX Aviation Warehouse"
        ]

        for part in self.data["parts"]:

            self.data["inventory"].append({
                "id": self.uuid(),
                "part_id": part["id"],
                "warehouse_name": random.choice(warehouses),
                "quantity_on_hand": random.randint(5, 250),
                "quantity_reserved": random.randint(0, 50),
                "reorder_point": random.randint(5, 40)
            })

    # -------------------------------------------------
    # ASSETS
    # -------------------------------------------------

    def generate_assets(self, assets_per_site=15):

        aircraft_models = [
            "Boeing 737 MAX",
            "Airbus A320",
            "Boeing 787",
            "Airbus A220",
            "Embraer E175"
        ]

        for site in self.data["sites"]:

            for _ in range(assets_per_site):

                self.data["assets"].append({
                    "id": self.uuid(),
                    "site_id": site["id"],
                    "serial_number": f"AC-{uuid.uuid4().hex[:10].upper()}",
                    "model": random.choice(aircraft_models),
                    "status": random.choice([
                        "active",
                        "maintenance",
                        "grounded"
                    ]),
                    "health_score": random.randint(55, 100),
                    "runtime_hours": random.randint(5000, 75000)
                })

    # -------------------------------------------------
    # WORK ORDERS
    # -------------------------------------------------

    def generate_work_orders(self, work_orders_per_asset=6):

        priorities = [
            "low",
            "medium",
            "high",
            "critical"
        ]

        statuses = [
            "open",
            "in_progress",
            "completed"
        ]

        issue_types = [
            "engine_vibration",
            "hydraulic_leak",
            "avionics_fault",
            "landing_gear_issue",
            "oil_pressure_warning",
            "temperature_alarm"
        ]

        for asset in self.data["assets"]:

            for _ in range(work_orders_per_asset):

                created_at = datetime.utcnow() - timedelta(
                    days=random.randint(1, 730)
                )

                started_at = created_at + timedelta(
                    hours=random.randint(1, 24)
                )

                finished_at = started_at + timedelta(
                    hours=random.randint(2, 96)
                )

                self.data["work_orders"].append({
                    "id": self.uuid(),
                    "asset_id": asset["id"],
                    "priority": random.choice(priorities),
                    "status": random.choice(statuses),
                    "issue_type": random.choice(issue_types),
                    "created_at": created_at.isoformat(),
                    "started_at": started_at.isoformat(),
                    "finished_at": finished_at.isoformat()
                })

    # -------------------------------------------------
    # ASSIGNMENTS
    # -------------------------------------------------

    def generate_assignments(self):

        user_ids = [u["id"] for u in self.data["users"]]

        for wo in self.data["work_orders"]:

            self.data["work_order_assignments"].append({
                "id": self.uuid(),
                "work_order_id": wo["id"],
                "user_id": random.choice(user_ids),
                "assigned_at": wo["created_at"]
            })

    # -------------------------------------------------
    # FAILURES / HISTORY / REFURBISHMENTS
    # -------------------------------------------------

    def generate_work_order_parts_and_failures(self):

        part_ids = [p["id"] for p in self.data["parts"]]

        failure_types = [
            "fatigue",
            "corrosion",
            "thermal_damage",
            "electrical_failure",
            "wear"
        ]

        severities = [
            "low",
            "medium",
            "high",
            "critical"
        ]

        conditions = [
            "new",
            "good",
            "degraded",
            "failed"
        ]

        event_types = [
            "installed",
            "removed",
            "replaced",
            "refurbished"
        ]

        for wo in self.data["work_orders"]:

            selected_parts = random.sample(
                part_ids,
                random.randint(1, 4)
            )

            for part_id in selected_parts:

                self.data["work_order_parts"].append({
                    "id": self.uuid(),
                    "work_order_id": wo["id"],
                    "part_id": part_id,
                    "quantity": random.randint(1, 5),
                    "consumed_at": wo["finished_at"]
                })

                self.data["component_failures"].append({
                    "id": self.uuid(),
                    "asset_id": wo["asset_id"],
                    "part_id": part_id,
                    "work_order_id": wo["id"],
                    "detected_at": wo["created_at"],
                    "failure_type": random.choice(failure_types),
                    "severity": random.choice(severities)
                })

                self.data["asset_component_history"].append({
                    "id": self.uuid(),
                    "asset_id": wo["asset_id"],
                    "part_id": part_id,
                    "work_order_id": wo["id"],
                    "event_type": random.choice(event_types),
                    "failure_type": random.choice(failure_types),
                    "from_timestamp": wo["started_at"],
                    "to_timestamp": wo["finished_at"],
                    "condition_before": random.choice(conditions),
                    "condition_after": random.choice(conditions),
                    "position": f"Slot-{random.randint(1, 12)}"
                })

                if random.random() < 0.35:

                    completed_at = (
                        datetime.fromisoformat(wo["finished_at"]) +
                        timedelta(days=random.randint(2, 30))
                    )

                    self.data["part_refurbishments"].append({
                        "id": self.uuid(),
                        "part_id": part_id,
                        "work_order_id": wo["id"],
                        "status": random.choice([
                            "received",
                            "repairing",
                            "completed"
                        ]),
                        "return_condition": random.choice(conditions),
                        "received_at": wo["finished_at"],
                        "completed_at": completed_at.isoformat()
                    })

    # -------------------------------------------------
    # MASTER
    # -------------------------------------------------

    def generate_all(self):

        self.generate_roles()
        self.generate_customers()
        self.generate_users()
        self.generate_sites()
        self.generate_parts()
        self.generate_inventory()
        self.generate_assets()
        self.generate_work_orders()
        self.generate_assignments()
        self.generate_work_order_parts_and_failures()

    # -------------------------------------------------
    # EXPORTS
    # -------------------------------------------------

    def export_json(self, filename='synthetic_data.json'):

        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2)

        print(f"Data exported to {filename}")

    def export_sql_inserts(self, filename='synthetic_data.sql'):

        def sql_value(v):

            if v is None:
                return 'NULL'

            if isinstance(v, (int, float, Decimal)):
                return str(v)

            escaped = str(v).replace("'", "''")

            return f"'{escaped}'"

        with open(filename, 'w') as f:

            for table_name, records in self.data.items():

                if not records:
                    continue

                f.write(f"\n-- {table_name}\n")

                for record in records:

                    columns = ', '.join(record.keys())

                    values = ', '.join([
                        sql_value(v)
                        for v in record.values()
                    ])

                    f.write(
                        f"INSERT INTO {table_name} ({columns}) VALUES ({values});\n"
                    )

        print(f"SQL exported to {filename}")


# -------------------------------------------------
# RUN
# -------------------------------------------------

if __name__ == '__main__':

    generator = SyntheticDatasetGenerator()

    generator.export_json()
    generator.export_sql_inserts()

    print("Synthetic dataset generation complete.")