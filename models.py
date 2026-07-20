import uuid

class Parcel:
    def __init__(self, sender, receiver, phone, address, pincode):
        self.tracking_id = str(uuid.uuid4())[:8].upper()
        self.sender = sender
        self.receiver = receiver
        self.phone = phone
        self.address = address
        self.pincode = pincode
        self.status = "Booked"

    def to_dict(self):
        return {
            "tracking_id": self.tracking_id,
            "sender": self.sender,
            "receiver": self.receiver,
            "phone": self.phone,
            "address": self.address,
            "pincode": self.pincode,
            "status": self.status
        }