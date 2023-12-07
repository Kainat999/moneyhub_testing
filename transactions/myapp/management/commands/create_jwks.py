import json
from django.core.management.base import BaseCommand
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

class Command(BaseCommand):
    help = 'Generate JWKS (JSON Web Key Set) for Moneyhub API Client'

    def handle(self, *args, **options):
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )

        private_key = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        public_key = key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        jwks = {
            "keys": [
                {
                    "kty": "RSA",
                    "n": key.public_key().public_numbers().n,
                    "e": key.public_key().public_numbers().e,
                    "kid": "DZ76sBMR0VNfmEJ3YZ6Frn_77qtKoBIlx9JGXlctt5s",  # CHange this later 
                    "use": "sig",
                    "alg": "RS256"
                }
            ]
        }

        print("Public keys:")
        print(json.dumps(jwks, indent=4))

        print("\nPrivate keys:")
        print(private_key.decode())

