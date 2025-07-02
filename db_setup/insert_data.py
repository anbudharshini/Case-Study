import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anburohan26*",
        database="CaseStudyCRS")

    cursor = conn.cursor()

    cursor.execute("ALTER TABLE vehicle AUTO_INCREMENT = 1")
    cursor.execute("ALTER TABLE customer AUTO_INCREMENT = 100")
    cursor.execute("ALTER TABLE lease AUTO_INCREMENT = 300")
    cursor.execute("ALTER TABLE payment AUTO_INCREMENT = 1000")

    vehicle_data = [
        ('Toyota', 'Corolla', 2020, 50.00, 'available', 5, 1.8),
        ('Honda', 'Civic', 2019, 48.00, 'available', 5, 2.0),
        ('Ford', 'Focus', 2021, 55.00, 'available', 5, 1.6),
        ('Hyundai', 'Elantra', 2022, 60.00, 'available', 5, 2.0),
        ('BMW', 'X5', 2021, 100.00, 'notavailable', 7, 3.0),
        ('Tesla', 'Model 3', 2023, 120.00, 'available', 5, 0.0),
        ('Kia', 'Seltos', 2020, 45.00, 'available', 5, 1.5),
        ('Mahindra', 'XUV700', 2022, 70.00, 'notavailable', 7, 2.2),
        ('Maruti', 'Swift', 2018, 35.00, 'available', 5, 1.2),
        ('Renault', 'Kiger', 2021, 40.00, 'available', 5, 1.0)
    ]
    cursor.executemany("""
        INSERT INTO vehicle (make, model, year, dailyrate, status, passengercapacity, enginecapacity)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, vehicle_data)

    customer_data = [
        ('John', 'Doe', 'john.doe@example.com', '9876543210'),
        ('Jane', 'Smith', 'jane.smith@example.com', '9123456780'),
        ('Raj', 'Kumar', 'raj.kumar@example.com', '9012345678'),
        ('Priya', 'Sharma', 'priya.sharma@example.com', '9345678901'),
        ('Anil', 'Mehta', 'anil.mehta@example.com', '9900112233'),
        ('Divya', 'Iyer', 'divya.iyer@example.com', '9871234560'),
        ('Vikram', 'Patel', 'vikram.patel@example.com', '9567890123'),
        ('Neha', 'Rao', 'neha.rao@example.com', '9887654321'),
        ('Karthik', 'Menon', 'karthik.menon@example.com', '9001122334'),
        ('Meena', 'Gupta', 'meena.gupta@example.com', '9456781234')
    ]
    cursor.executemany("""
        INSERT INTO customer (firstname, lastname, email, phonenumber)
        VALUES (%s, %s, %s, %s)
    """, customer_data)

    cursor.execute("SELECT vehicleid FROM vehicle ORDER BY vehicleid ASC LIMIT 10")
    vehicle_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT customerid FROM customer ORDER BY customerid ASC LIMIT 10")
    customer_ids = [row[0] for row in cursor.fetchall()]

    lease_data = [
        (vehicle_ids[0], customer_ids[0], '2025-06-01', '2025-06-05', 'dailylease'),
        (vehicle_ids[1], customer_ids[1], '2025-06-02', '2025-06-30', 'monthlylease'),
        (vehicle_ids[2], customer_ids[2], '2025-06-10', '2025-06-15', 'dailylease'),
        (vehicle_ids[3], customer_ids[3], '2025-06-01', '2025-06-30', 'monthlylease'),
        (vehicle_ids[4], customer_ids[4], '2025-06-12', '2025-06-16', 'dailylease'),
        (vehicle_ids[5], customer_ids[5], '2025-06-20', '2025-07-20', 'monthlylease'),
        (vehicle_ids[6], customer_ids[6], '2025-06-03', '2025-06-08', 'dailylease'),
        (vehicle_ids[7], customer_ids[7], '2025-06-05', '2025-07-05', 'monthlylease'),
        (vehicle_ids[8], customer_ids[8], '2025-06-07', '2025-06-14', 'dailylease'),
        (vehicle_ids[9], customer_ids[9], '2025-06-09', '2025-07-09', 'monthlylease')
    ]
    cursor.executemany("""
        INSERT INTO lease (vehicleid, customerid, startdate, enddate, type)
        VALUES (%s, %s, %s, %s, %s)
    """, lease_data)

    cursor.execute("SELECT leaseid FROM lease ORDER BY leaseid ASC LIMIT 10")
    lease_ids = [row[0] for row in cursor.fetchall()]

    payment_data = [
        (lease_ids[0], '2025-06-05', 250.00),
        (lease_ids[1], '2025-06-30', 1400.00),
        (lease_ids[2], '2025-06-15', 275.00),
        (lease_ids[3], '2025-06-30', 1800.00),
        (lease_ids[4], '2025-06-16', 300.00),
        (lease_ids[5], '2025-07-20', 2400.00),
        (lease_ids[6], '2025-06-08', 225.00),
        (lease_ids[7], '2025-07-05', 2600.00),
        (lease_ids[8], '2025-06-14', 210.00),
        (lease_ids[9], '2025-07-09', 3000.00)
    ]
    cursor.executemany("""INSERT INTO payment (leaseid, paymentdate, amount)VALUES (%s, %s, %s)""", payment_data)

    conn.commit()
    print("All data inserted successfully.")

except mysql.connector.Error as err:
    print("MySQL Error:", err)
    if conn:
        conn.rollback()

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed.")
