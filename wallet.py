from rsa import sign
# === Wallet ===
def create_transaction(wallet_private_key, sender_public_key, receiver_public_key, sender, receiver, amount):
    document = f"{sender}->{receiver}->{amount}"
    signature = sign(wallet_private_key, document)
    return {
        'sender_public_key': sender_public_key,
        'receiver_public_key': receiver_public_key,
        'sender': sender,
        'receiver': receiver,
        'amount': amount,
        'document': document,
        'signature': signature
    }

