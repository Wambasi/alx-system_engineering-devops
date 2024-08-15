Issue Summary
Duration: The outage lasted 1 hour and 35 minutes, from 14:10 to 15:45 UTC on August 10, 2024.
Impact: The main e-commerce platform became significantly slow, leading to an average page load time of over 30 seconds. Approximately 85% of users experienced delays, with 50% unable to complete their purchases during the outage. The issue affected the checkout process, resulting in a temporary loss of revenue and a significant drop in user satisfaction.
Root Cause: The root cause was an unanticipated overload on the primary database server due to an unexpected spike in traffic combined with a malfunctioning load balancer that failed to redistribute the traffic to the secondary database server.

Timeline
14:10 UTC: Issue detected by the monitoring system, which triggered alerts for high response times across the platform.
14:12 UTC: Engineering team received automated alerts from the monitoring system regarding increased response times and began investigating the issue.
14:15 UTC: Initial investigation suggested that a recent code deployment might be causing the issue. The deployment was rolled back, but the problem persisted.
14:25 UTC: The database server was identified as the potential bottleneck. Logs showed a significant increase in read and write operations.
14:30 UTC: The team assumed a potential DDoS attack due to the unusual spike in traffic and began mitigating this possibility.
14:40 UTC: Traffic patterns were analyzed, showing legitimate user traffic rather than a DDoS attack. Focus shifted back to the database and load balancer.
14:50 UTC: Escalation to the DevOps team for deeper investigation into the load balancer and database server configuration.
15:10 UTC: The load balancer was found to be malfunctioning, failing to route traffic to the secondary database server, leading to overload on the primary server.
15:20 UTC: Load balancer configuration was corrected, and traffic began to properly distribute between both database servers.
15:30 UTC: System performance started improving, with page load times returning to normal levels.
15:45 UTC: The issue was fully resolved, and all systems were functioning normally.





Root Cause and Resolution
The issue was caused by an unexpected spike in legitimate user traffic, which overloaded the primary database server. The load balancer, which was configured to distribute traffic between two database servers, malfunctioned and failed to direct any traffic to the secondary server. This led to the primary database server becoming a bottleneck, significantly slowing down the platform's response times.
To resolve the issue, the DevOps team corrected the configuration of the load balancer, ensuring that traffic was evenly distributed between the primary and secondary database servers. Once the traffic distribution was balanced, the load on the primary server decreased, and the platform's performance returned to normal.

Corrective and Preventative Measures
Improvements/Fixes:
Load Balancer Configuration: Review and update the load balancer configuration to ensure proper failover and load distribution.
Database Scalability: Enhance database scalability to handle unexpected traffic spikes, including the possibility of auto-scaling.
Monitoring Enhancements: Implement more granular monitoring of the load balancer to detect failures more quickly.
Tasks:
Patch Load Balancer Software: Update the load balancer software to the latest version to address any known bugs.
Add Redundancy: Introduce an additional failover load balancer to handle traffic in case of primary load balancer failure.
Stress Testing: Conduct regular stress testing to simulate traffic spikes and ensure the system can handle them without degrading performance.
Monitoring Alerts: Create specific alerts for load balancer performance and database server load to detect issues early.
