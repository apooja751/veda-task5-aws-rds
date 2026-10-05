## veda-task5-aws-rds

# Veda Technology Cloud Computing Internship — Task 5

## AWS RDS Database Deployment and EC2 Application Integration

### Objective

Deploy a managed MySQL database using Amazon RDS and connect it securely with an Amazon EC2 application server.

## AWS Services Used

- Amazon RDS (MySQL)
- Amazon EC2
- Amazon VPC
- Amazon Security Groups

## Implementation

- Created an Amazon RDS MySQL database.
- Configured database backup and encryption.
- Created an EC2 application server using Amazon Linux.
- Configured separate security groups for EC2 and RDS.
- Restricted RDS MySQL access to the EC2 application security group.
- Connected the EC2 instance to RDS using the MySQL client.
- Created a database table and inserted test data.
- Developed a Python application to read and write data from RDS.
- Verified successful database connectivity and data retrieval.

## Database Configuration

| Configuration | Value |
|---|---|
| Database Engine | MySQL |
| Database Name | task5db |
| Instance Class | db.t3.micro |
| Region | Mumbai (ap-south-1) |
| Storage | 20 GiB |
| Backup Retention | 1 Day |

## Security

The RDS security group allows MySQL traffic on port `3306` only from the EC2 application security group.

SSH access to the EC2 instance is restricted to the user's IP address.

## Application Test

The Python application successfully connected to Amazon RDS, inserted data, and retrieved the stored records.

Example output:

```text
(1, 'Veda Task 5 - RDS connection successful')
(2, 'Hello from Python App - Veda Task 5')

```

## Project Repository Structure

```text
veda-task5-aws-rds/
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── 1-A-task5-rds-connectivity-security.png
    ├── 1-B-task5-rds-connectivity-security.png
    ├── 2-A-task5-rds-database-backup-config.png
    ├── 2-B-task5-rds-database-backup-config.png
    ├── 2-C-task5-rds-database-backup-config.png
    ├── 3-task5-rds-database-available.png
    ├── 4-task5-rds-connection-details.png
    ├── 5-task5-app-ec2-running.png
    ├── 6-task5-rds-data-read-write-success.png
    ├── 7-task5-python-app-rds-success.png
    ├── 8-task5-app-security-group-final.png
    └── 9-task5-rds-security-group-final.png

```
##Screenshots
Screenshots documenting the implementation are included in the repository.

##Conclusion
Task 5 successfully demonstrated the deployment of a managed MySQL database using Amazon RDS and its secure integration with an EC2-based Python application.
