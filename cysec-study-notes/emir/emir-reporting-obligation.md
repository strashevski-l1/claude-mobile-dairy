> [Study notes](../README.md) › [Advanced](../advanced.md) › [EMIR: Derivatives, Clearing and CCPs](README.md) › Trade reporting  
> Source: <https://www.exampasscy.com/study-notes/emir/emir-reporting-obligation>

CySEC Advanced · Chapter 10 · Topic 2 of 7

# Who must report derivatives to a trade repository, and who is liable?

The reporting duty and its deadline, who reports for small non-financial counterparties and for funds since 18 June 2020, the third-country and intragroup reliefs, the 2024 reporting standards and EMIR 3's data-quality rules, and Refit's changes for CCPs. · By the [ExamPass CY editorial team](../about.md) · Last reviewed 30 September 2026 · 8 min read

Tested in: Advanced · Ch 10

<a id="short-answer"></a>

## Short answer

Counterparties and CCPs report every derivative, OTC or exchange-traded, to a **trade repository** by the **working day after** it is concluded, modified or terminated. Counterparties keep records for at least **five years** after the contract ends. Since **18 June 2020**, a **financial counterparty** alone reports, and is liable for, its OTC trades with a **non-financial counterparty below the clearing thresholds**, unless that firm opts to report itself. The **UCITS management company** or **AIFM** reports a fund's OTC contracts. Since **29 April 2024** reports use **ISO 20022** and **203 fields**. Delegation does not shift responsibility.

<a id="key-facts"></a>

## Trade reporting at a glance

| Point | Rule |
| --- | --- |
| Who and what | Counterparties and CCPs, for every derivative contract, OTC or exchange-traded |
| Deadline | No later than the working day after conclusion, modification or termination |
| Records | Counterparties keep them for at least five years after the contract ends; CCPs keep theirs for at least ten (Article 29) |
| FC trading OTC with an NFC- | Since 18 June 2020 the FC reports both sides and is liable; the NFC- supplies data the FC cannot be expected to have, or chooses to report itself after telling the FC |
| Funds | For OTC contracts: UCITS, the management company; AIF, the AIFM; IORP without legal personality, the entity managing it |
| Intragroup | No reporting of trades within a fully consolidated group under centralised risk procedures, where at least one party is an NFC and the parent is not an FC, unless the notified authorities disagree within three months |
| Standards since 29 April 2024 | ISO 20022 XML; 203 fields (129 before); UTI and UPI rules; significant errors notified promptly to the competent authority |
| EMIR 3, since 24 December 2024 | Data-quality procedures; the duty to report correctly and without duplication now expressly covers delegated reporting; periodic penalties up to 1% of average daily turnover, for up to six months, for repeated systematic manifest errors |
| CCPs (Refit, 18 December 2019) | Margin simulation tool for clearing members, at portfolio level with scenarios since 24 December 2024; insolvency law cannot block porting of client positions |

Source: EMIR, Articles 9, 12(1a), 29, 38(6) and 39(11), as amended by Regulations (EU) 2019/834 and 2024/2987; Delegated Regulation (EU) 2022/1855; Implementing Regulation (EU) 2022/1860, Article 9; CySEC Circulars C593 and C633.

<a id="in-the-exam"></a>

## In the exam

The exam is written from the exam material, which does not reflect the changes below. Expect its answer. If that answer is not among the options and the current rule is, choose the current rule.

- **Margin simulation tool**

  **Exam material:** From 18 December 2019 a CCP gives its clearing members a tool that works out, on a gross basis, the extra initial margin a new transaction might trigger.

  **Current law (since 24 December 2024 (Regulation (EU) 2024/2987, EMIR 3); the tool itself since 18 December 2019 (Regulation (EU) 2019/834, EMIR Refit)):** The tool works at portfolio level and simulates margin requirements under different scenarios. Access is still secured, and the results are not binding.

  Both texts require the tool; what changed is its portfolio basis and the added scenarios.

<a id="who-reports"></a>

## What must be reported, and who has reported since 18 June 2020?

Under Article 9, counterparties and CCPs must make sure that the details of every derivative contract they conclude, and of any modification or termination, reach a trade repository no later than the following working day. The repository must be registered by ESMA or, if it is in a third country, recognised by ESMA. The duty covers exchange-traded as well as OTC derivatives. Counterparties keep records for at least five years after the contract ends, and CCPs for at least ten (Article 29). Reporting may be delegated, for example to the other party or to a service provider, but counterparties and CCPs must still ensure that reports are correct and not duplicated.

Refit reallocated the duty, and the exam material rightly dates this to 18 June 2020. When a financial counterparty (FC) concludes an OTC contract with a non-financial counterparty below the clearing thresholds (NFC-), the FC alone reports for both sides and is legally liable for the accuracy of the details. The NFC- must give the FC any details the FC cannot reasonably be expected to hold, and answers for those. An NFC- that has already invested in its own reporting system may instead report its OTC trades with FCs itself, after telling them; it then carries the liability. For funds' OTC contracts the manager is responsible and liable: the management company for a UCITS, the AIFM for an AIF, and the managing entity for an occupational pension fund (IORP) without legal personality.

Two reliefs complete the picture. An NFC- trading with a firm in a third country need not report if that firm would be an FC were it established in the EU and has reported under its own regime to a repository that must give EU authorities direct and immediate access to the data. Before 24 December 2024 this also required a Commission equivalence decision; EMIR 3 removed that condition. Within a group, contracts where at least one party is an NFC need not be reported if both parties are fully consolidated and subject to centralised risk procedures and the parent is not an FC. The parties notify their competent authorities, and the exemption stands unless those authorities disagree within three months. Since 24 December 2024, where an NFC above a clearing threshold uses this exemption, its EU parent reports that NFC's net aggregate positions by class of derivatives to the parent's competent authority every week. That authority passes them to ESMA and to the NFC's authority.

Terms used in this note

- **NFC-** — A non-financial counterparty whose positions do not exceed any clearing threshold.

- **UTI** — Unique trade identifier: the single code both counterparties use to identify a reported contract.

- **UPI** — Unique product identifier: a global code identifying the type of OTC derivative product.

- **Systematic manifest errors** — Obvious reporting errors that recur; since 24 December 2024 they must lead to penalties.

<a id="reporting-standards"></a>

## What changed in April 2024 and under EMIR 3?

Since 29 April 2024 reports have followed new technical standards: Delegated Regulation (EU) 2022/1855 sets their content and Implementing Regulation (EU) 2022/1860 their format. Reports use ISO 20022 XML and contain 203 fields instead of 129, with rules on generating the unique trade identifier (UTI), a unique product identifier (UPI), separate collateral data and a field naming the entity responsible for reporting. Trades still outstanding had to be updated to the new standard within 180 days. The entity responsible for reporting must promptly notify its competent authority of misreporting that affects many reports, of obstacles that stop reports reaching the repository on time, and of other significant reporting errors. CySEC's Circulars C593 and C633 ask firms to use ESMA's notification template and send it to CySEC's dedicated EMIR mailbox.

EMIR 3 added duties from 24 December 2024. Counterparties and CCPs must have procedures and arrangements to ensure the quality of the data they report. Where reports repeatedly contain systematic manifest errors, the competent authority must impose penalties; a periodic penalty payment can reach 1% of the entity's average daily turnover in the previous business year for each day the breach continues, for up to six months. In Cyprus, CySEC's general fining powers also apply to the firms it supervises.

<a id="ccp-changes"></a>

## Which Refit changes affected CCPs?

The exam material lists two CCP changes that applied from 18 December 2019. First, a CCP must give its clearing members a simulation tool showing how much additional initial margin it might call if they cleared a new trade. Following Refit's wording, the exam material says the tool works on a gross basis. Since 24 December 2024 EMIR 3 has required the tool to work at portfolio level and to simulate margin under different scenarios. As before, access is secured and the results are not binding. Second, national insolvency law may not prevent a CCP from porting a defaulting clearing member's client positions and assets to another clearing member, or from returning what is left to the clients, under Article 48(5) to (7). Refit also required CCPs to explain their initial margin models, a duty EMIR 3 has made more detailed; see [What must a CCP disclose, to whom, and when can a breach stay private?](ccp-transparency-and-disclosure.md)

<a id="how-to-think"></a>

## How to think about it

Ask three questions. What is reported? Every derivative, on or off exchange, by the next working day. Who submits it? Normally each counterparty, but the FC for OTC trades with a small NFC, and the manager for a fund's OTC trades. Who is liable? Whoever the Regulation names, even if the task has been delegated. Then add the newer layers: new formats since April 2024, prompt notice of significant errors, and penalties for repeated systematic errors since December 2024.

<a id="common-mistakes"></a>

## Common mistakes

1. **Assuming the small NFC reports its own OTC trades with an FC.** Since 18 June 2020 the FC reports and is liable, unless the NFC has chosen to report itself.
2. **Thinking a fund reports for itself.** The UCITS management company or the AIFM is responsible and liable for the fund's OTC contracts.
3. **Treating delegation as a transfer of liability.** A counterparty may outsource the task but must still ensure reports are correct and not duplicated.
4. **Quoting the gross-basis simulation tool as current.** Since 24 December 2024 the tool works at portfolio level and includes scenario simulations.

<a id="legal-references"></a>

## Legal references

- [Regulation (EU) No 648/2012 on OTC derivatives, central counterparties and trade repositories (EMIR), consolidated version of 17 January 2025](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02012R0648-20250117)

  Article 9 (reporting obligation) · Article 12(1a) (penalties for systematic manifest errors) · Article 38(6) (simulation tool) · Article 39(11) (insolvency law)
- [Regulation (EU) 2019/834 amending EMIR (EMIR Refit)](https://eur-lex.europa.eu/eli/reg/2019/834/oj)

  Article 2 (application of the reporting changes from 18 June 2020 and the CCP changes from 18 December 2019)
- [Regulation (EU) 2024/2987 amending EMIR (EMIR 3)](https://eur-lex.europa.eu/eli/reg/2024/2987/oj)

  Article 1 (amendments to Articles 9, 12 and 38) · Article 5 (application)
- [Delegated Regulation (EU) 2022/1855 (details to be reported to trade repositories), applicable from 29 April 2024](https://eur-lex.europa.eu/eli/reg_del/2022/1855/oj)

  Fields and content of reports
- [Implementing Regulation (EU) 2022/1860 (reporting standards, formats and methods), applicable from 29 April 2024](https://eur-lex.europa.eu/eli/reg_impl/2022/1860/oj)

  Formats; Article 9 (notification of errors and omissions)
- [CySEC Circular C593 (3 August 2023): new EMIR reporting standards from 29 April 2024](https://www.cysec.gov.cy/CMSPages/GetFile.aspx?guid=5f407056-588f-44b9-bcae-66eea9184959)
- [CySEC Circular C633 (16 April 2024): notifying errors and omissions in EMIR reporting](https://www.cysec.gov.cy/CMSPages/GetFile.aspx?guid=7c114ecc-8d2a-4a66-9698-cb6b12cba961)

<a id="related-h"></a>

## Related topics

Topic 1. **[What is EMIR for, and how has it changed since 2012?](emir-purpose-and-framework.md)** — EMIR's three aims and the tools that serve them, trade repositories, the main amending acts, and CySEC's role and fines.

Topic 7. **[What must a CCP disclose, to whom, and when can a breach stay private?](ccp-transparency-and-disclosure.md)** — What a CCP and its clearing members make public, what goes to ESMA and the competent authority, and when a member's breach stays private.

Topic 3. **[Which OTC derivatives must be centrally cleared, and by whom?](emir-clearing-obligation.md)** — The classes declared for clearing, who is in scope, the clearing thresholds, the four-month phase-in, active accounts and the exemptions.

---

[← Previous topic Purpose and framework](emir-purpose-and-framework.md) | [Next topic: Clearing obligation →](emir-clearing-obligation.md)
