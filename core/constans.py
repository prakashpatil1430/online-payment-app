ACCOUNT_STATUS = (
    ('active', 'Active'),
    ('in-active', 'In-cctive'),
)

MARITAL_STATUS = (
    ('married', 'Married'),
    ('single', 'Single'),
    ('other', 'Other'),
)

GENDER = (
    ('male', "Male"),
    ("female", "Female"),
    ("other", "Other")
)

NATIONALITY_CHOICES = [
    ('united status', 'United States'),
    ('united kingdom', 'United Kingdom'),
    ('canada', 'Canada'),
    ('australia', 'Australia'),
    ('india', 'India'),
]

IDENTITY_TYPE = (
    ("adhar_card", "Adhar Card"),
    ("driving_licience", "Driving Licence"),
    ("international_passport", "Innternational Passport"),
)

ACCOUNT_STATUS = [
    ('in-active', 'In-Active'),
    ('active', 'Active'),
    # Add more choices as needed
]


TRANSACTION_TYPE = (
    ("transfer", "Transfer"),
    ("recieved", "Recieved"),
    ("withdraw", "withdraw"),
    ("refund", "Refund"),
    ("request", "Payment Request"),
    ("none", "None")
)

TRANSACTION_STATUS = (
    ("failed", "failed"),
    ("completed", "completed"),
    ("pending", "pending"),
    ("processing", "processing"),
    ("request_sent", "request_sent"),
    ("request_settled", "request settled"),
    ("request_processing", "request processing"),

)


CARD_TYPE = (
    ("master", "master"),
    ("visa", "visa"),
    ("verve", "verve"),

)


NOTIFICATION_TYPE = (
    ("None", "None"),
    ("Transfer", "Transfer"),
    ("Credit Alert", "Credit Alert"),
    ("Debit Alert", "Debit Alert"),
    ("Sent Payment Request", "Sent Payment Request"),
    ("Recieved Payment Request", "Recieved Payment Request"),
    ("Funded Credit Card", "Funded Credit Card"),
    ("Withdrew Credit Card Funds", "Withdrew Credit Card Funds"),
    ("Deleted Credit Card", "Deleted Credit Card"),
    ("Added Credit Card", "Added Credit Card"),

)
