---
id: 18903834277661
title: Customer test environment
url: https://support.nepton.com/hc/en-gb/articles/18903834277661-Customer-test-environment
locale: en-gb
category: Support
category_id: 360000446658
section: Servers and data protection
section_id: 360005870038
section_path:
- Servers and data protection
labels: []
promoted: false
updated_at: '2026-03-10T07:14:28Z'
edited_at: '2026-03-10T07:13:58Z'
---

# Customer test environment

A customer test environment is an optional extra that can be added to your service agreement which provides you with a dedicated, risk-free, sandbox environment, where you can practice or test anything you like outside of production environment. If you would like to add this service to your subscription, please contact Nepton customer service or your nominated project manager.
# About customer test environments
Customer test environments are available 24/7 and are completely isolated from other environments. These environments run alongside your production environment and receive the same software updates same time as your production environment.
Your testing data is preserved and safely separated from your production environment. When importing test data consider GDPR and use anonymized data. 
There is no connection between your test environment and your production environment.
# Setup
Customer test environments are self-managed and persistent. You have full control over what you do there, what configuration is present, and what data is present. All functionalities you have in production are also available in test. Please read the related common uses and best practices heading below for more information.
# Common uses & best practices
## Update configuration to match production
If you already have production environment that has worktime settings groups, those can be copied. However exceptional settings and some customization can't be copied. 
Worktime > Administration > Setting Groups, choosing "Add Setting group", and picking the "Create from System Identifier" option. By carefully selecting the Setting group copied, you can target a specific part of your configuration, or the entire configuration by selecting the root node, and checking the Copy Subgroups option. 
After copying is done, these settings are totally independent. This means all changes need to be done separately both your production and test environment if you like to have a full copy of setting environment in test up to date.
You can now create, or move existing, testing users into the desired setting groups, and make any desired changes in the configuration for testing.
## Update data to match production
When importing data to your test environment please carefully consider GDPR. Testing should not be done against real personal information. We recommend anonymizing data, before importing it to your testing environment. 
## Test integration changes
We recommend testing integrations against other test environments to keep data in production in safe. Integrations are set up like in production. You find guidance in our support page. Integrations can be scheduled or manually executed. 
Note: When creating integrations base in those that are in test environment to production remember change IPs, end-points and other configurations.
## Practice and training
Training staff in a production environment is risky, plus, without letting them get hands-on with the service, it is hard to achieve learning objectives and knowledge retention. The customer test environment is the perfect place to tackle this, where you can freely configure, simulate, edit, and reset, as much as you like, any time you like, without any risk.
A common way to do this, is to create dedicated personal accounts for your trainees, then create supporting settings and additional test users for their manipulation based on your production environment and training needs. The test users and environment persist until you choose to clean them, so trainees can even revisit the training area safely in their own time.
