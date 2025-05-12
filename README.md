<h1> Cloud Security Project – AWS CloudFormation & S3 Management </h1>


<h2>Description</h2>
This project reflects my personal experience working with AWS to automate infrastructure and improve cloud security practices using AWS CloudFormation, Amazon S3, and EC2 services. I focused on creating, updating, and tearing down cloud resources through infrastructure-as-code (IaC) methods while ensuring secure and scalable deployment.
<br />


<h2>Key Tasks Performed</h2>

- <b>✅ Task 1: Create an S3 Bucket Using AWS CloudFormation</b>

I launched a CloudFormation stack that provisioned an S3 bucket automatically.

<p align="center">
  <img src="https://i.imgur.com/zteEDBE.png" alt="Screenshot description" width="80%" />
</p>

- 📁 <b> Task 2: Delete the Stack and Verify Deletion</b>

I deleted the stack using CloudFormation and confirmed that the associated S3 bucket was removed.

<p align="center">
  <img src="https://i.imgur.com/19xuVJM.png" alt="Screenshot description" width="80%" />
</p>

- <b> 📥 Task 3: Use a Different Template to Re-Create Stack</b>
  
I tested a modified CloudFormation template to recreate the infrastructure and observed how changes impacted the deployment.

<p align="center">
  <img src="https://i.imgur.com/D7R54vi.png" alt="Screenshot description" width="80%" />
</p>
<p align="center">
  <img src="https://i.imgur.com/NhH28wN.png" alt="Screenshot description" width="80%" />
</p>

- <b> 🌐 Task 4: Provision a Web Application</b>
  
I provisioned an EC2 instance with outputs including VPC and public subnet information. The web server was accessible via the URL output in CloudFormation.

<p align="center">
  <img src="https://i.imgur.com/6WnI1RD.png" alt="Screenshot description" width="80%" />
</p>

<p align="center">
  <img src="https://i.imgur.com/bJSZdB3.png" alt="Screenshot description" width="80%" />
</p>

<p align="center">
  <img src="https://i.imgur.com/cEGx4Le.png" alt="Screenshot description" width="80%" />
</p>

- <b> 🔁 Task 5: Update Existing Stack Resources</b>

I modified an existing CloudFormation stack to update EC2 instance configurations and validate the changes.

<p align="center">
  <img src="https://i.imgur.com/mPwGJ4m.png" alt="Screenshot description" width="80%" />
</p>

## 💡 Technologies & Tools Used

- **AWS CloudFormation**
- **Amazon S3**
- **Amazon EC2**
- **VPC**
- **Infrastructure as Code (IaC)**
- **AWS Console**

## 📌 Summary

This project gave me practical, hands-on experience in deploying secure and manageable cloud infrastructure using AWS services. It reinforced the importance of automation, consistency, and resource lifecycle management in real-world cloud environments.





<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
