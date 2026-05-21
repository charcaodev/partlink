"""
Database Connection Test Script
Run this to verify your DATABASE_URL is correct and the connection works
"""

import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

def test_database_connection():
    """Test database connection with detailed error reporting"""
    
    # Load environment variables
    load_dotenv()
    
    DATABASE_URL = os.getenv("DATABASE_URL")
    
    print("=" * 60)
    print("DATABASE CONNECTION TEST")
    print("=" * 60)
    
    # Check 1: Environment variable exists
    if not DATABASE_URL:
        print("❌ FAILED: DATABASE_URL is not set in environment variables")
        print("\nMake sure you have a .env file with DATABASE_URL defined")
        return False
    
    print(f"✓ DATABASE_URL found in environment")
    
    # Mask sensitive info for display
    if "@" in DATABASE_URL:
        parts = DATABASE_URL.split("@")
        masked_url = parts[0].split(":")[0] + ":****@" + parts[1]
    else:
        masked_url = DATABASE_URL[:20] + "****"
    
    print(f"  URL format: {masked_url}")
    
    # Check 2: URL format validation
    valid_prefixes = ['postgresql://', 'postgresql+psycopg2://', 'mysql://', 
                      'mysql+pymysql://', 'sqlite:///', 'mssql://', 'oracle://']
    
    if not any(DATABASE_URL.startswith(prefix) for prefix in valid_prefixes):
        print(f"⚠️  WARNING: URL doesn't start with common database prefix")
        print(f"   Common formats:")
        print(f"   - PostgreSQL: postgresql://user:pass@host:port/dbname")
        print(f"   - MySQL: mysql://user:pass@host:port/dbname")
        print(f"   - SQLite: sqlite:///path/to/database.db")
    
    # Check 3: Create engine
    try:
        print("\n✓ Creating SQLAlchemy engine...")
        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
            echo=False  # Set to True for SQL query debugging
        )
        print("✓ Engine created successfully")
    except Exception as e:
        print(f"❌ FAILED to create engine: {e}")
        return False
    
    # Check 4: Test connection
    try:
        print("\n✓ Attempting to connect to database...")
        with engine.connect() as connection:
            print("✓ Connection established!")
            
            # Check 5: Execute a simple query
            print("\n✓ Running test query...")
            result = connection.execute(text("SELECT 1"))
            result.fetchone()
            print("✓ Query executed successfully")
            
            # Check 6: Get database version/info
            try:
                if 'postgresql' in DATABASE_URL:
                    version_result = connection.execute(text("SELECT version()"))
                    version = version_result.fetchone()[0]
                    print(f"\n✓ Database: PostgreSQL")
                    print(f"  Version: {version.split(',')[0]}")
                elif 'mysql' in DATABASE_URL:
                    version_result = connection.execute(text("SELECT VERSION()"))
                    version = version_result.fetchone()[0]
                    print(f"\n✓ Database: MySQL")
                    print(f"  Version: {version}")
                elif 'sqlite' in DATABASE_URL:
                    version_result = connection.execute(text("SELECT sqlite_version()"))
                    version = version_result.fetchone()[0]
                    print(f"\n✓ Database: SQLite")
                    print(f"  Version: {version}")
            except Exception as e:
                print(f"  (Could not retrieve version info: {e})")
            
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED - Database connection is working!")
        print("=" * 60)
        return True
        
    except Exception as e:
        print(f"\n❌ CONNECTION FAILED: {e}")
        print("\nCommon issues:")
        print("  - Check username/password are correct")
        print("  - Verify host and port are accessible")
        print("  - Ensure database exists")
        print("  - Check firewall/security group settings")
        print("  - Verify SSL requirements (add ?sslmode=require if needed)")
        return False
    
    finally:
        engine.dispose()


if __name__ == "__main__":
    success = test_database_connection()
    exit(0 if success else 1)