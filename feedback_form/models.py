from django.db import models


class Feedback(models.Model):
    BRANCH_CHOICES = [
       
        ('Adayar', 'Adayar'),
        ('Alwarpet', 'Alwarpet'),
        ('Ambattur', 'Ambattur'),
        ('Anna Nagar', 'Anna Nagar'),
        ('Ashok Nagar', 'Ashok Nagar'),
        ('Avadi', 'Avadi'),
        ('Ayanavaram', 'Ayanavaram'),
        ('Bazullah Road', 'Bazullah Road'),
        ('Besant Nagar', 'Besant Nagar'),
        ('Chrompet', 'Chrompet'),
        ('Egmore', 'Egmore'),
        ('Kanchipuram', 'Kanchipuram'),
        ('Kanchi Gandhi Road', 'Kanchi Gandhi Road'),
        ('Karapakkam', 'Karapakkam'),
        ('Kathipara', 'Kathipara'),
        ('Kelambakkam', 'Kelambakkam'),
        ('Korattur', 'Korattur'),
        ('Luz New', 'Luz New'),
        ('Madipakkam', 'Madipakkam'),
        ('Medavakkam', 'Medavakkam'),
        ('Mogappair', 'Mogappair'),
        ('Mylapore', 'Mylapore'),
        ('Nanganallur', 'Nanganallur'),
        ('Nanganallur West', 'Nanganallur West'),
        ('Nungambakkam', 'Nungambakkam'),
        ('Perambur', 'Perambur'),
        ('Porur', 'Porur'),
        ('Pondicherry', 'Pondicherry'),
        ('Purasai Palace', 'Purasai Palace'),
        ('Saidapet', 'Saidapet'),
        ('Tambaram West', 'Tambaram West'),
        ('Thiruvallur', 'Thiruvallur'),
        ('Thiruvanmiyur', 'Thiruvanmiyur'),
        ('Thiruvannamalai', 'Thiruvannamalai'),
        ('Thuraipakkam', 'Thuraipakkam'),
        ('Triplicane', 'Triplicane'),
        ('Usman Road', 'Usman Road'),
        ('Vadapalani', 'Vadapalani'),
        ('Valasaravakkam', 'Valasaravakkam'),
        ('Velachery', 'Velachery'),
        ('Villivakkam', 'Villivakkam'),
        ('VN Road T.Nagar', 'VN Road T.Nagar'),
        ('Venus Colony', 'Venus Colony'),
        ('West Mambalam', 'West Mambalam'),
        ('Chennai Airport', 'Chennai Airport'),
    
    ]

    FEEDBACK_CHOICES = [
        ('excellent', 'Excellent'),
        ('satisfied', 'Satisfied'),
        ('to_be_improved', 'To be Improved'),
    ]

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    value_for_money = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    packaging = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    quality = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    display = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    variety = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    comments = models.TextField(blank=True, null=True)
    employee_name_and_id = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    anniversary = models.DateField(blank=True, null=True)
    voice_recording = models.FileField(upload_to='recordings/', blank=True, null=True)

    def __str__(self):
        return f"Feedback from {self.name} - {self.branch}"
