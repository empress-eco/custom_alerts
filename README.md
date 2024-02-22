<div align="center">
  <img src="https://grow.empress.eco/uploads/default/original/2X/1/1f1e1044d3864269d2a613577edb9763890422ab.png" alt="Project Logo">
  <p align="center">
    Enhance your user experience with personalized, timely alerts.
    <br />
    <a href="https://empress.eco/">Visit our Website</a>
    ·
    <a href="https://github.com/empress-eco/custom_alerts/issues/new?assignees=empress-eco&labels=bug&template=bug_report.md&title=%5BBUG%5D">Report a Bug</a>
    ·
    <a href="https://github.com/empress-eco/custom_alerts/issues/new?assignees=empress-eco&labels=enhancement&template=feature_request.md&title=%5BFEATURE%5D">Request a Feature</a>
    ·
    <a href="https://grow.empress.eco/">Get Support</a>
  </p>
</div>

## About Custom Alerts

Custom Alerts is a powerful module designed to streamline communications on your platform. It provides personalized alerts to specific recipients upon login, enhancing user experience and ensuring timely information delivery. 

### Key Features
- Customizable alert types with unique display properties and sounds.
- Alerts are tailored to user roles, ensuring only relevant users receive specific alerts.
- Alerts have a specific duration and can be set to repeat a specific number of times.

## Technical Stack and Setup Instructions

Custom Alerts is built on Empress, a full-stack web application framework. 

### Prerequisites
Ensure you have Empress version v12.0.0 or above.

### Installation

To install, follow these simple steps:

1. Open your terminal
2. Navigate to the bench directory
```sh
cd ~/Empress-bench
```
3. Execute the following commands, replacing `[sitename]` with the name of your site:
```sh
bench get-app https://github.com/empress-eco/custom_alerts.git
bench build --app alerts
bench --site [sitename] install-app alerts
```

### Usage

After installation, create and customize your alerts. 

1. Navigate to `Alert Type` to create a new alert type.
2. Customize the display priority, sound, and look of the alerts.
3. Go to `Alert` to create a new alert entry.
4. Select an `Alert Type`, set the alert duration, and specify the alert recipients.
5. After submitting the alert, check the `Seen By` table to monitor alert reach.

## Contribution Guidelines

We welcome your contributions! To contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License and Acknowledgements

This project is under the MIT License. Your contributions are also licensed under the MIT License.

Special thanks to the Empress Community for their foundational contributions. Their innovation and dedication have been instrumental in building the foundations and functionalities we rely on. We are profoundly grateful for their pioneering work and ongoing support.

We also want to acknowledge and thank our contributors [avc](https://github.com/git-avc), [lan9635](https://github.com/lan9635), and [satishkakani](https://github.com/satishkakani) for their valuable input and support in debugging and testing.