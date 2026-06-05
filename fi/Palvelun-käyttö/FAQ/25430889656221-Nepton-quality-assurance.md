---
id: 25430889656221
title: Nepton quality assurance
url: https://support.nepton.com/hc/fi/articles/25430889656221-Nepton-quality-assurance
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: FAQ
section_id: 360000934177
section_path:
- FAQ
labels:
- Testing
- Quality assurance
promoted: false
updated_at: '2025-02-28T13:59:05Z'
edited_at: '2025-02-28T13:59:05Z'
---

# Nepton quality assurance

Tätä artikkelia ei ole vielä käännetty suomeksi.
With hundreds of thousands of active users, Nepton must take quality and availability very seriously to offer a good service, whilst continually adding, improving, and evolving, features.
# Uptime & Platform status
We strive to avoid all downtime, but as with all digital services, there is a need for interruptions from time to time. Whenever possible, these are planned in advance and with at least two weeks notice. Otherwise, we utilise the regular maintenance slots. The [Platform status](<https://support.nepton.com/hc/en-gb/articles/360006554777>) page details all current and planned events, plus maintenance and release windows, during which service availability can be affected.
To ensure good monitoring and prompt reactions to problems, we utilise a third-party uptime monitoring service which automatically informs key Nepton staff when there are problems. In turn, the Platform status page is updated with information about these events. Please sign-in and [follow](<https://support.nepton.com/hc/en-gb/articles/4406604045585>) it to be informed of any new events.
# Quality Assurance & Testing
Quality assurance at Nepton already begins during the refinement of requirements and is a theme throughout the entire development process. As such, the notes below also roughly describe our internal development workflow.
## Requirements refinement
All changes and new features begin with establishing an understanding of the reasons behind a need and then identifying how that can be tackled with Nepton or what could change to close the gap. For this to happen efficiently we also nominate an internal business owner of each topic at this early stage. They will oversee the process and ensure focus, whilst also ensuring the original requirements are not lost to the details.
Once the "Why" and "What" have been well understood, the technical specialists are involved and a "How" is formed. Basic mock-ups and design work is often created to facilitate this. This combination of knowledge is then ticketed to form a well justified and explained set of requirements.
## Kick off
For efficiency and a better overall result, we group related tasks and topics and try to handle them all together in one go. For example, everything needed for a new feature set, or to complete a customer on-boarding project. As such, we allocate the business owner a dedicated team who will focus on each development topic until it's completion.
## Iterative implementation
The technical team work closely with the business owner and technical product owner who give feedback and steer the work towards success. The developers maximise the opportunities for internal feedback with iterative implementation based on an approved implementation plan.
Local testing includes continuous integration with our suite of hundreds of thousands of automated testing assertions. During this phase, iterative technical reviews are held weekly, focusing on Nepton best practices and conventions covering code style, code quality, compliance, security, and performance.
## Usability & Acceptance
Although there is iterative feedback during implementation, it ultimately culminates with a final round of usability and acceptance testing by the business owner. All requirements are ensured to have been met, and the changes "feel good" when in use.
## Technical Acceptance
With the requirements having been met, it is time to ensure that all technical considerations are sound and in keeping with Nepton practices. Whilst most of this is ensured during development by iterative feedback and reviews, plus automated testing with hundreds of thousands of assertions; This phase provides a final step of oversight and tweaks.
A fresh round of automated testing is also used during this phase to identify any obvious performance, security or regression problems that have raised as a result of the combined changes.
## Manual Testing
For large, complex, or breaking changes, we include a round of human testing and fixing before release. Usually, this is carried out before the release date is announced, and these tests predominantly focus on topics which are difficult to automatically test, such as UI styling, usability, and workflow considerations.
We also get so-called "hallway usability testing" by involving Nepton specialists who were not involved in the development process earlier.
For a planned weekend updates there can be hundreds of staff hours spent on the manual testing effort before a service update is approved.
## Staging, Communications, and Release
With a changeset completely tested, approved and ready, the update is planned and communicated to customers and all specialists. For larger or breaking changes that will be released over a weekend, we always strives to communicate these at least two weeks in advance so that there is time to prepare and react.
Wherever there are significant changes or new features added to the service we always strive to provide a newsletter and webinar covering all the most meaningful details, and to give a practical example of how they benefit the community.
The Nepton release process is fully automated, but always attended by technical specialists. In the event of problems or failures, we have well established play books for disaster recovery and communication.
# Customer testing
Typically, customers do not need to perform any additional testing for new releases. The Nepton quality assurance process described above makes sure that updates are of the best quality we can reasonably provide.
As a standard practice, any new worktime settings are always introduced in a way that ensures they do not affect existing customer configurations. This means that customers can rely on the stability of their settings without needing to verify changes before they are applied.
However, if you wish to confirm that a release has had no impact on your Nepton configuration, the best approach is to compare reports generated before and after the release.
Nepton processes worktime interpretation in real-time. This means that any worktime setting changes without a specified validity date will affect all recorded worktime. While changes to setting behaviour due to a release are extremely rare, they would be reflected in worktime data if they occurred.
To verify that a release has not affected your worktime data, follow these best practices:
  1. Select a reporting period that has already been approved and where users are no longer recording worktime.
  2. Recommended reports for comparison: Hours by salary type & Exceptional entries report
  3. Download the same report for the same period both before and after the release.
  4. Use Spreadsheet Compare in Excel to quickly identify any differences.


As a paid service, Nepton also provides [Customer Test Environments](<https://support.nepton.com/hc/en-gb/articles/18903834277661-Customer-test-environment>) for testing setting changes, integration testing, and trainings. These are primarily intended for testing your own planned changes to configurations and integrations. They are updated at the same time as your production environment.
# Customer development cooperation
For more complex changes that require external services (such as SSO), we offer [Public Testing Servers (PTS)](<https://support.nepton.com/hc/en-gb/articles/18904657842973-Public-Testing-Servers-aka-PTS>). These environments alsos enable collaboration with invited stakeholders during feature development and advanced testing and feedback sessions.
