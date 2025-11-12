# ISO/IEC 25010 Metrics and Evaluation Mapping
## ON-CARE System Quality Assessment Framework

---

## Table of Contents
1. [ISO 25010 Complete Metrics Structure](#iso-25010-complete-metrics-structure)
2. [ISO 9126 to ISO 25010 Mapping](#iso-9126-to-iso-25010-mapping)
3. [Evaluation Data Alignment](#evaluation-data-alignment)
4. [ISO 25010 Evaluation Framework](#iso-25010-evaluation-framework)

---

## ISO 25010 Complete Metrics Structure

### ISO/IEC 25010 Product Quality Model (8 Characteristics)

#### 1. **Functional Suitability**
**Sub-characteristics:**
- **Functional Completeness**: Degree to which the set of functions covers all the specified tasks and user objectives
- **Functional Correctness**: Degree to which a product or system provides the correct results with the needed degree of precision
- **Functional Appropriateness**: Degree to which the functions facilitate the accomplishment of specified tasks and objectives

**Evaluation Metrics:**
- Function coverage percentage
- Requirement fulfillment rate
- Error rate in functional outputs
- Task completion success rate

---

#### 2. **Performance Efficiency**
**Sub-characteristics:**
- **Time Behaviour**: Degree to which the response and processing times and throughput rates of a product or system, when performing its functions, meet requirements
- **Resource Utilization**: Degree to which the amounts and types of resources used by a product or system, when performing its functions, meet requirements
- **Capacity**: Degree to which the maximum limits of a product or system parameter meet requirements

**Evaluation Metrics:**
- Response time (average, 95th percentile)
- Throughput (transactions per second)
- CPU utilization percentage
- Memory usage
- Storage efficiency
- Concurrent user capacity

---

#### 3. **Compatibility**
**Sub-characteristics:**
- **Co-existence**: Degree to which a product can perform its required functions efficiently while sharing a common environment and resources with other products, without detrimental impact on any other product
- **Interoperability**: Degree to which two or more systems, products or components can exchange information and use the information that has been exchanged

**Evaluation Metrics:**
- System integration success rate
- Data exchange compatibility
- API compatibility score
- Cross-platform compatibility

---

#### 4. **Usability**
**Sub-characteristics:**
- **Appropriateness Recognizability**: Degree to which users can recognize whether a product or system is appropriate for their needs
- **Learnability**: Degree to which a product or system can be used by specified users to achieve specified goals of learning to use the product or system with effectiveness, efficiency, freedom from risk and satisfaction in a specified context of use
- **Operability**: Degree to which a product or system has attributes that make it easy to operate and control
- **User Error Protection**: Degree to which a system protects users against making errors
- **User Interface Aesthetics**: Degree to which a user interface enables pleasing and satisfying interaction for the user
- **Accessibility**: Degree to which a product or system can be used by people with the widest range of characteristics and capabilities to achieve a specified goal in a specified context of use

**Evaluation Metrics:**
- Task completion time
- Number of user errors
- User satisfaction score (Likert scale)
- Learning curve measurement
- Accessibility compliance score (WCAG)
- Interface usability score

---

#### 5. **Reliability**
**Sub-characteristics:**
- **Maturity**: Degree to which a system, product or component meets needs for reliability under normal operation
- **Availability**: Degree to which a system, product or component is operational and accessible when required for use
- **Fault Tolerance**: Degree to which a system, product or component operates as intended despite the presence of hardware or software faults
- **Recoverability**: Degree to which, in the event of an interruption or failure, a product or system can recover the data directly affected and re-establish the desired state of the system

**Evaluation Metrics:**
- Mean Time Between Failures (MTBF)
- System uptime percentage
- Error detection rate
- Recovery time
- Data loss prevention rate
- Fault tolerance level

---

#### 6. **Security**
**Sub-characteristics:**
- **Confidentiality**: Degree to which a product or system ensures that data are accessible only to those authorized to have access
- **Integrity**: Degree to which a system, product or component prevents unauthorized access to, or modification of, computer programs or data
- **Non-repudiation**: Degree to which actions or events can be proven to have taken place, so that the events or actions cannot be repudiated later
- **Accountability**: Degree to which the actions of an entity can be traced uniquely to the entity
- **Authenticity**: Degree to which the identity of a subject or resource can be proved to be the one claimed

**Evaluation Metrics:**
- Security vulnerability count
- Authentication success rate
- Data encryption coverage
- Access control effectiveness
- Audit trail completeness
- Security compliance score (HIPAA, GDPR, etc.)

---

#### 7. **Maintainability**
**Sub-characteristics:**
- **Modularity**: Degree to which a system or computer program is composed of discrete components such that a change to one component has minimal impact on other components
- **Reusability**: Degree to which an asset can be used in more than one system, or in building other assets
- **Analysability**: Degree of effectiveness and efficiency with which it is possible to assess the impact on a product or system of an intended change, or to diagnose a product for deficiencies or causes of failures, or to identify parts to be modified
- **Modifiability**: Degree to which a product or system can be effectively and efficiently modified without introducing defects or degrading existing product quality
- **Testability**: Degree of effectiveness and efficiency with which test criteria can be established for a system, product or component, and tests can be performed to determine whether those criteria have been met

**Evaluation Metrics:**
- Code modularity score
- Component reusability percentage
- Bug detection time
- Code modification time
- Test coverage percentage
- Code complexity metrics (Cyclomatic Complexity)

---

#### 8. **Portability**
**Sub-characteristics:**
- **Adaptability**: Degree to which a product or system can be effectively and efficiently adapted for different or evolving hardware, software or other operational or usage environments
- **Installability**: Degree of effectiveness and efficiency with which a product or system can be successfully installed and/or uninstalled in a specified environment
- **Replaceability**: Degree to which a product can replace another specified software product for the same purpose in the same environment

**Evaluation Metrics:**
- Platform compatibility count
- Installation success rate
- Configuration time
- Migration effort
- Cross-platform functionality

---

### ISO/IEC 25010 Quality in Use Model (5 Characteristics)

#### 1. **Effectiveness**
- Accuracy and completeness with which users achieve specified goals

#### 2. **Efficiency**
- Resources expended in relation to the accuracy and completeness with which users achieve goals

#### 3. **Satisfaction**
- **Usefulness**: Degree to which a user is satisfied with their perceived achievement of pragmatic goals, including the results of use and the consequences of use
- **Trust**: Degree to which a user or other stakeholder has confidence that a product or system will behave as intended
- **Pleasure**: Degree to which a user obtains pleasure from fulfilling their personal needs
- **Comfort**: Degree to which a user is satisfied with physical comfort

#### 4. **Freedom from Risk**
- **Economic Risk Mitigation**: Degree to which a product or system mitigates the potential risk to financial status, financial operations, owned property, or individuals in the intended contexts of use
- **Health and Safety Risk Mitigation**: Degree to which a product or system mitigates the potential risk to people in the intended contexts of use
- **Environmental Risk Mitigation**: Degree to which a product or system mitigates the potential risk to property or the environment in the intended contexts of use

#### 5. **Context Coverage**
- **Context Completeness**: Degree to which a product or system can be used with effectiveness, efficiency, freedom from risk and satisfaction in all the specified contexts of use
- **Flexibility**: Degree to which a product or system can be used with effectiveness, efficiency, freedom from risk and satisfaction in contexts beyond those initially specified

---

## ISO 9126 to ISO 25010 Mapping

### Mapping Your Current Evaluation to ISO 25010

| ISO 9126 (Current) | ISO 25010 (Updated) | Mapping Notes |
|-------------------|---------------------|---------------|
| **Functionality** | **Functional Suitability** | Direct mapping with enhanced sub-characteristics |
| **Reliability** | **Reliability** | Similar structure, minor enhancements |
| **Usability** | **Usability** | Similar structure, expanded sub-characteristics |
| **Efficiency** | **Performance Efficiency** | Renamed, similar focus |
| **Maintainability** | **Maintainability** | Similar structure |
| **Portability** | **Portability** | Similar structure |
| *(Not in ISO 9126)* | **Compatibility** | NEW - Important for healthcare systems |
| *(Not in ISO 9126)* | **Security** | NEW - Critical for healthcare/pharmaceutical systems |

---

## Evaluation Data Alignment

### Your Current Results (ISO 9126) → ISO 25010 Translation

#### **Table: Current ISO 9126 Evaluation Summary**

| Criteria | Mean | Interpretation | ISO 25010 Equivalent |
|----------|------|----------------|---------------------|
| Functionality | 4.67 | HIGHLY ACCEPTABLE | Functional Suitability |
| Reliability | 4.76 | HIGHLY ACCEPTABLE | Reliability |
| Usability | 4.60 | HIGHLY ACCEPTABLE | Usability |
| Efficiency | 4.82 | HIGHLY ACCEPTABLE | Performance Efficiency |
| Maintainability | 4.35 | ACCEPTABLE | Maintainability |
| Portability | 4.24 | ACCEPTABLE | Portability |
| **Total Mean** | **4.57** | **HIGHLY ACCEPTABLE** | **Overall Quality Score** |

---

### Recommended ISO 25010 Evaluation Framework

#### **Table 1.0: Functional Suitability Evaluation (Office Staff)**

| Sub-characteristic | Evaluation Criteria | 5 | 4 | 3 | 2 | 1 |
|-------------------|---------------------|---|---|---|---|---|
| **Functional Completeness** | Provides order management functionality | | | | | |
| | Generates correct program outputs | | | | | |
| | Provides quick navigation to important order list | | | | | |
| **Functional Correctness** | System outputs match expected results | | | | | |
| | Data validation prevents incorrect entries | | | | | |
| | Calculations are accurate (pricing, inventory) | | | | | |
| **Functional Appropriateness** | Functions support order processing workflow | | | | | |
| | System features match user needs | | | | | |

**Current Data Mapping:**
- Your "Functionality" data (Mean: 4.67) maps to **Functional Suitability**
- Office Staff: 4.56
- Sales Agent: 4.63
- Manager: 4.83

---

#### **Table 2.0: Reliability Evaluation (Office Staff)**

| Sub-characteristic | Evaluation Criteria | 5 | 4 | 3 | 2 | 1 |
|-------------------|---------------------|---|---|---|---|---|
| **Maturity** | System operates without frequent errors | | | | | |
| **Availability** | System is accessible when needed | | | | | |
| **Fault Tolerance** | Detects program errors immediately | | | | | |
| | Provides error-free notifications | | | | | |
| **Recoverability** | System recovers from errors gracefully | | | | | |
| | Provides program output based on expected result | | | | | |

**Current Data Mapping:**
- Your "Reliability" data (Mean: 4.76) maps to **Reliability**
- Office Staff: 4.63
- Sales Agent: 4.86
- Manager: 4.80

---

#### **Table 3.0: Usability Evaluation (Office Staff)**

| Sub-characteristic | Evaluation Criteria | 5 | 4 | 3 | 2 | 1 |
|-------------------|---------------------|---|---|---|---|---|
| **Learnability** | Can be understood, learned, and used easily | | | | | |
| **Operability** | Provides on-screen prompts and messages that are clear | | | | | |
| **User Error Protection** | System prevents user errors effectively | | | | | |
| **User Interface Aesthetics** | Interface appears attractive to users | | | | | |
| **Accessibility** | Provides relevant instructional guide | | | | | |

**Current Data Mapping:**
- Your "Usability" data (Mean: 4.60) maps to **Usability**
- Office Staff: 4.53
- Sales Agent: 4.63
- Manager: 4.63

---

#### **Table 4.0: Performance Efficiency Evaluation (Office Staff)**

| Sub-characteristic | Evaluation Criteria | 5 | 4 | 3 | 2 | 1 |
|-------------------|---------------------|---|---|---|---|---|
| **Time Behaviour** | Order creation and update done in shortest time possible | | | | | |
| **Resource Utilization** | Minimizes storage resource for the application | | | | | |
| **Capacity** | System handles concurrent users effectively | | | | | |

**Current Data Mapping:**
- Your "Efficiency" data (Mean: 4.82) maps to **Performance Efficiency**
- Office Staff: 4.80
- Sales Agent: 4.85
- Manager: 4.80

---

#### **Table 5.0: Maintainability Evaluation (Office Staff)**

| Sub-characteristic | Evaluation Criteria | 5 | 4 | 3 | 2 | 1 |
|-------------------|---------------------|---|---|---|---|---|
| **Analysability** | Allows users to easily identify code errors within application | | | | | |
| | Provides comments of program codes for ease of understanding | | | | | |
| **Modifiability** | Modification of code for enhancement can be done | | | | | |
| **Testability** | System components can be tested independently | | | | | |

**Current Data Mapping:**
- Your "Maintainability" data (Mean: 4.35) maps to **Maintainability**
- Office Staff: 4.40
- Sales Agent: 4.33
- Manager: 4.33

---

#### **Table 6.0: Portability Evaluation (Office Staff)**

| Sub-characteristic | Evaluation Criteria | 5 | 4 | 3 | 2 | 1 |
|-------------------|---------------------|---|---|---|---|---|
| **Adaptability** | Adapts for new versions of operating systems | | | | | |
| **Installability** | Allows installation of plug-ins for integration | | | | | |
| **Replaceability** | Automatically updates program components in any OS | | | | | |

**Current Data Mapping:**
- Your "Portability" data (Mean: 4.24) maps to **Portability**
- Office Staff: 4.30
- Sales Agent: 4.33
- Manager: 4.10

---

### **NEW: Additional ISO 25010 Characteristics**

#### **Table 7.0: Compatibility Evaluation**

| Sub-characteristic | Evaluation Criteria | 5 | 4 | 3 | 2 | 1 |
|-------------------|---------------------|---|---|---|---|---|
| **Co-existence** | System works alongside other software without conflicts | | | | | |
| **Interoperability** | Can exchange data with other systems (pharmacy systems, payment gateways) | | | | | |
| | API integration works with third-party services | | | | | |

**Recommendation:** Add this evaluation to your assessment.

---

#### **Table 8.0: Security Evaluation**

| Sub-characteristic | Evaluation Criteria | 5 | 4 | 3 | 2 | 1 |
|-------------------|---------------------|---|---|---|---|---|
| **Confidentiality** | Patient/prescription data is protected | | | | | |
| **Integrity** | Data cannot be modified without authorization | | | | | |
| **Authenticity** | User authentication is reliable | | | | | |
| **Accountability** | System logs all user actions (audit trail) | | | | |
| **Non-repudiation** | Actions can be proven to have occurred | | | | | |

**Recommendation:** **CRITICAL** for healthcare systems - Add this evaluation immediately.

---

## ISO 25010 Evaluation Framework

### Revised Evaluation Summary Table

#### **Table 26.0: Summary of Software Evaluation on ON-CARE (ISO 25010)**

| ISO 25010 Characteristic | Mean | Interpretation | Notes |
|-------------------------|------|----------------|-------|
| **Functional Suitability** | 4.67 | HIGHLY ACCEPTABLE | Mapped from Functionality |
| **Reliability** | 4.76 | HIGHLY ACCEPTABLE | Direct mapping |
| **Usability** | 4.60 | HIGHLY ACCEPTABLE | Direct mapping |
| **Performance Efficiency** | 4.82 | HIGHLY ACCEPTABLE | Mapped from Efficiency |
| **Compatibility** | *TBD* | *To Be Evaluated* | **NEW - Required** |
| **Maintainability** | 4.35 | ACCEPTABLE | Direct mapping |
| **Portability** | 4.24 | ACCEPTABLE | Direct mapping |
| **Security** | *TBD* | *To Be Evaluated* | **NEW - Critical for Healthcare** |
| | | | |
| **Total Mean (6 evaluated)** | **4.57** | **HIGHLY ACCEPTABLE** | Based on existing 6 criteria |
| **Total Mean (8 evaluated)** | *TBD* | *To Be Calculated* | After adding Compatibility & Security |

---

### Recommendations for Your Research

1. **Update Methodology Section:**
   - Change references from "ISO 9126" to "ISO/IEC 25010"
   - Explain that ISO 25010 is the current standard (replaced ISO 9126 in 2011)
   - Add rationale for using ISO 25010

2. **Add Missing Evaluations:**
   - **Security** (Critical for healthcare systems)
   - **Compatibility** (Important for system integration)

3. **Update Evaluation Tables:**
   - Rename "Functionality" to "Functional Suitability"
   - Rename "Efficiency" to "Performance Efficiency"
   - Add sub-characteristics for each main characteristic

4. **Update Interpretation:**
   - In your results, mention: "Based on ISO/IEC 25010 Product Quality Model, the system achieved..."
   - Note that 6 out of 8 characteristics were evaluated
   - Recommend future evaluation of Security and Compatibility

5. **Academic Writing:**
   - Cite ISO/IEC 25010:2011 standard
   - Explain why ISO 25010 is more comprehensive than ISO 9126
   - Mention that Security and Compatibility are critical additions for healthcare systems

---

### Likert Scale Interpretation (ISO 25010 Context)

| Scale | Interpretation | Weighted Mean Range |
|-------|----------------|-------------------|
| 5 | Strongly Agree | 4.50 - 5.00 |
| 4 | Agree | 3.50 - 4.49 |
| 3 | Moderately Agree | 2.50 - 3.49 |
| 2 | Disagree | 1.50 - 2.49 |
| 1 | Strongly Disagree | 1.00 - 1.49 |

**Your Current Results:**
- **HIGHLY ACCEPTABLE**: Functional Suitability (4.67), Reliability (4.76), Usability (4.60), Performance Efficiency (4.82)
- **ACCEPTABLE**: Maintainability (4.35), Portability (4.24)

---

## References

- ISO/IEC 25010:2011 - Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models
- ISO/IEC 9126-1:2001 - Software engineering — Product quality — Part 1: Quality model (Superseded by ISO 25010)

---

*This document provides a comprehensive mapping from ISO 9126 to ISO 25010 and evaluation framework for the ON-CARE Medicine Ordering System.*

