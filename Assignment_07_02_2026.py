import hashlib
import secrets
import hmac

class PasswordAuthenticator:
    def __init__(self):
      
        self.user_db = {}

    def register_user(self, username, password):
        """Registers a new user by generating a salt and hashing the password."""
        if username in self.user_db:
            return False, "Error: Username already exists."

       
        salt = secrets.token_hex(16)

        
        hashed_password = self._hash_password(password, salt)

       
        self.user_db[username] = {
            'salt': salt,
            'hash': hashed_password
        }
        return True, f"Success: User '{username}' registered securely."

    def authenticate_user(self, username, password):
        """Authenticates a user by comparing the provided password's hash to the stored hash."""
        
        generic_error = "Error: Invalid username or password."

        if username not in self.user_db:
            return False, generic_error

        stored_salt = self.user_db[username]['salt']
        stored_hash = self.user_db[username]['hash']

        
        attempted_hash = self._hash_password(password, stored_salt)

       
        if hmac.compare_digest(stored_hash, attempted_hash):
            return True, "Success: Authentication verified."
        else:
            return False, generic_error

    def _hash_password(self, password, salt):
        """Core hashing logic using PBKDF2 with SHA-256."""
       
        iterations = 100000
        
        derived_key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            iterations
        )
        return derived_key.hex()


if __name__ == "__main__":
    auth = PasswordAuthenticator()

    print("--- 1. User Registration ---")
    success, msg = auth.register_user("admin_user", "Tr0ub4dor&3!")
    print(msg)
    
   
    success, msg = auth.register_user("admin_user", "AnotherPassword123")
    print(msg)

    print("\n--- 2. User Authentication ---")
    
    success, msg = auth.authenticate_user("admin_user", "Tr0ub4dor&3!")
    print(f"Login Attempt (Correct): {msg}")

  
    success, msg = auth.authenticate_user("admin_user", "WrongPassword!")
    print(f"Login Attempt (Wrong Password): {msg}")

  
    success, msg = auth.authenticate_user("ghost_user", "Tr0ub4dor&3!")
    print(f"Login Attempt (Wrong Username): {msg}")