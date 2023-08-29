## Automated Testing Project using Page Object Pattern

The objective of this project was to establish an automated testing framework based on the Page Object pattern, aimed at enhancing the maintainability, readability, and stability of our test cases. This project adhered to a set of guiding principles, ensuring the effectiveness and reliability of the implemented testing procedures:

- **Base Layer Abstraction**: A foundational layer known as the "Base Page" was developed to consolidate common functionalities, including wait operations, logging mechanisms, and exception screenshot handling. By doing so, redundant code was minimized, and the reusability of code components was significantly improved.

- **Page Object Pattern**: Embracing the Page Object pattern, the project employed the encapsulation of page element locators and action methods within dedicated page objects. This architectural approach effectively segregated test cases from the underlying page structure, resulting in enhanced maintainability of test scripts.

- **Data-Driven Testing**: To enable flexible testing scenarios, the separation of test data into distinct data files facilitated data-driven testing. This approach ensured that modifications to test data could be made seamlessly without impacting the core test cases.

- **Fixture Utilization**: The incorporation of fixture mechanisms, encompassing both setup and teardown procedures, played a crucial role in initializing and cleaning the testing environment. This not only bolstered the control and stability of tests but also ensured consistent test results.

- **Relative Locator Emphasis**: With a focus on resilience to changes in page structure, the preference for relative locators for element identification was emphasized. This approach increased the robustness of element selection.

- **Logging and Screenshot Capabilities**: Enhanced logging mechanisms were integrated to provide clear insights into the status and outcomes of test executions. Moreover, an automated screenshot functionality was introduced to capture the state of the page during the occurrence of issues. These features expedited the identification and resolution of issues, thereby elevating the overall quality and maintainability of tests.

[![framework.png](https://i.postimg.cc/mry6ytvF/framework.png)](https://postimg.cc/d7DBqttq)

By meticulously adhering to these guiding principles and incorporating advanced logging and screenshot functionalities, the ultimate goal of the project was realized—a robust, maintainable, and stable automated testing framework, ensuring the reliability of test cases within dynamic and evolving applications.
