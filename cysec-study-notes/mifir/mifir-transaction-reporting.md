> [Study notes](../README.md) › [Advanced](../advanced.md) › [MiFIR: Transparency, Reporting and Derivatives](README.md) › Transaction reporting  
> Source: <https://www.exampasscy.com/study-notes/mifir/mifir-transaction-reporting>

CySEC Advanced · Chapter 8 · Topic 7 of 9

# Which transactions must be reported to CySEC, by when, and how?

The reporting deadline, which instruments are in scope, what a report contains today, transmitted orders, the three reporting channels and their duties, error correction, branches and data sharing. · By the [ExamPass CY editorial team](../about.md) · Last reviewed 30 September 2026 · 9 min read

Tested in: Advanced · Ch 8, Basic · Ch 4

<a id="short-answer"></a>

## Short answer

An investment firm that executes transactions reports complete and accurate details to its competent authority **as quickly as possible** and no later than the **close of the following working day**. Reports cover instruments **traded on a venue** or admitted to trading there, and instruments whose **underlying**, index or basket is venue-traded, **whether the trade was on a venue or OTC**. The firm may report **itself**, through an **ARM** or through the **trading venue**, but still checks the reports. Whoever submits a report **corrects its errors**. ARMs have been authorised by **ESMA** since **1 January 2022**.

<a id="key-facts"></a>

## Transaction reporting at a glance

| Point | Rule |
| --- | --- |
| Deadline | As quickly as possible, and no later than the close of the following working day |
| Instruments in scope | Traded on a venue, admitted to trading or awaiting admission; underlying traded on a venue; underlying index or basket of venue-traded instruments; on venue or OTC |
| Main content (RTS 22) | Instrument, quantity, date and time, price; client identity, with an LEI for legal persons; people and algorithms behind the decision and the execution; waiver used; firm identifiers; short-sale flag for shares and sovereign debt |
| Transmitted orders | Pass all reportable details to the executing firm, or report the executed order as a transaction yourself |
| Channels | Directly, through an ARM acting on its behalf, or through the venue on whose system the trade was executed; the firm is not responsible for failures attributable to the ARM or venue but must check the reports |
| Venues reporting for firms | Secure, authenticated transfer; limited risk of corrupted data and unauthorised access; leakage prevented; adequate resources and back-up facilities |
| Errors | Corrected by whoever submitted the report, which sends a corrected report |
| ARMs | Authorised and supervised by ESMA since 1 January 2022, except derogated ARMs, supervised nationally (in Cyprus, CySEC) |

Source: MiFIR, Articles 26, 27b and 27i, as amended by Regulations (EU) 2019/2175 and 2024/791; Delegated Regulation (EU) 2017/590 (RTS 22).

<a id="in-the-exam"></a>

## In the exam

The exam is written from the exam material, which does not reflect the changes below. Expect its answer. If that answer is not among the options and the current rule is, choose the current rule.

- **Who authorises ARMs**

  **Exam material:** CySEC may approve reporting or trade-matching systems, registered or recognised trade repositories among them, as ARMs.

  **Current law (since 1 January 2022 (Regulation (EU) 2019/2175)):** ESMA authorises and supervises ARMs. Only ARMs with a derogation are authorised and supervised nationally, in Cyprus by CySEC.
- **Sharing reports with ESMA**

  **Exam material:** CySEC makes the reported information available to ESMA on request.

  **Current law (since 1 January 2022 (Regulation (EU) 2019/2175)):** Competent authorities make all reported information available to ESMA without undue delay.
- **Who has the security duties**

  **Exam material:** The security duties for reports made on behalf of investment firms fall on 'trading firms'.

  **Current law (since 3 January 2018 (MiFIR, Article 26(7))):** They fall on trading venues that report for investment firms. ARMs have their own security duties under Article 27i.
- **Transaction-type designation**

  **Exam material:** Reports of trades executed on a trading venue carry a designation of the transaction type.

  **Current law (since 3 January 2018 (MiFIR, Article 26(3))):** The designation is required for trades not carried out on a trading venue.

<a id="what-and-when"></a>

## Which transactions must be reported, and by when?

Under Article 26(1), an investment firm that executes transactions in financial instruments must report complete and accurate details to its competent authority as quickly as possible, and no later than the close of the following working day. The scope in Article 26(2) is broad. It covers instruments traded on a trading venue or admitted to trading there, including those awaiting admission; instruments whose underlying is traded on a venue; and instruments whose underlying is an index or basket made up of venue-traded instruments. A derivative on a listed share is therefore reportable even if the derivative itself is not traded on any venue. The duty applies whether the transaction is executed on a venue or not. This is still the rule in practice. The 2024 review narrows it for some OTC derivatives, but only once RTS 22 is revised, and ESMA put that revision on hold in June 2025.

When a firm transmits an order to another firm for execution, it either passes on all the details needed for the report, so that the executing firm can report, or it reports the executed order itself as a transaction, stating that it relates to a transmitted order. Trades carried out through a venue's systems by members or participants that are not subject to MiFIR are reported by the venue.

Terms used in this note

- **ARM** — Approved reporting mechanism: submits transaction reports to the authorities on behalf of investment firms.

- **LEI** — Legal entity identifier: the global 20-character code identifying a legal person.

- **RTS 22** — Delegated Regulation (EU) 2017/590, which sets the fields and format of transaction reports.

<a id="report-content"></a>

## What does a report contain?

The content is set in Article 26(3) and, in detail, in RTS 22. A report gives the instrument, the quantity, the date and time of execution and the price. It identifies the client for whom the trade was done, with a legal entity identifier (LEI) for clients that are legal persons, and the people and algorithms in the firm that took the investment decision and that executed it. It shows the waiver under which the trade took place, identifies the firms involved and, for shares and sovereign debt, flags whether the trade was a short sale. For commodity derivatives it shows whether the trade objectively and measurably reduces risk. Trades not executed on a trading venue also carry a flag showing the transaction type. The exam material ties that flag to trades executed on a venue; Article 26(3) has attached it to trades outside a venue since MiFIR first applied on 3 January 2018.

The 2024 review rewrote Article 26(3), but RTS 22 has not been amended, so firms still report the fields above, including the waiver and short-sale flags.

<a id="channels"></a>

## Who may submit reports, and who is responsible?

A firm may report itself, through an ARM that acts for it, or through the venue on whose system the trade was executed. It is not responsible for failures attributable to the ARM or venue, but must take reasonable steps to check the reports made for it. A venue that reports for firms needs sound security that keeps the transfer channel secure and authenticated, limits the risk of corrupted data and unauthorised access, and prevents leakage of information, plus adequate resources and back-up facilities. The exam material puts this duty on "trading firms" reporting for investment firms; Article 26(7) puts it on trading venues. A firm reporting through a trade repository that is approved as an ARM has met its duty once the report reaches the authority in time. Errors or omissions are corrected by whoever submitted the report, which sends a corrected report.

The exam material says CySEC may approve reporting or trade-matching systems, trade repositories among them, as ARMs. That sentence survives in Article 26(7), but since 1 January 2022 ARMs have been authorised and supervised by ESMA under Article 27b, except derogated ARMs, which national authorities supervise (in Cyprus, CySEC). Under Article 27i an ARM reports by the end of the following working day, checks reports for completeness and obvious errors, and keeps sound security, governed since 17 January 2025 by the Digital Operational Resilience Act (DORA). See also [What are APAs, ARMs and CTPs, and who supervises them today?](../cypriot-investment-firms/data-reporting-service-providers.md)

<a id="data-sharing-and-branches"></a>

## Who receives the data, and where do branches report?

The authority that receives reports makes sure the authority of the most relevant market by liquidity also receives them. The exam material says CySEC gives the information to ESMA on request. That was the rule until 31 December 2021. Since 1 January 2022 authorities have made all reported information available to ESMA without undue delay. The 2024 review adds that reports must also reach the authorities of transmitting firms, of branches involved and of the venues used. ESMA has said that, until a revised RTS 22 applies, reports are shared as before.

Transactions executed wholly or partly through a branch are reported to the authority of the firm's home Member State. RTS 22 has required this since 3 January 2018, unless the home and host authorities agree otherwise. The 2024 review wrote this rule into Article 26(8), together with another rule RTS 22 has applied since 2018: branches of third-country firms report to the authority that authorised them. Where a host authority such as CySEC receives branch reports under MiFID II, it passes them to the home authority unless that authority does not want them. The rule concerns investment firms' branches, not trading venues.

<a id="how-to-think"></a>

## How to think about it

Ask five questions. Is the instrument in scope: on a venue, or with a venue-traded underlying, index or basket? If so, on-venue or OTC makes no difference for now. Who reports: the executing firm, unless a transmitting firm reports instead, or the venue for members outside MiFIR. What goes in: the RTS 22 fields. When: by the close of the next working day. Through whom: the firm, an ARM or the venue, with the firm still checking and the submitter correcting its own errors.

<a id="common-mistakes"></a>

## Common mistakes

1. **Thinking that using an ARM moves all responsibility.** The firm must still check reports made for it; only failures attributable to the ARM or venue are excused.
2. **Naming CySEC as today's authoriser of ARMs.** ESMA has authorised and supervised them since 1 January 2022, except derogated ARMs.
3. **Dropping the fields removed at Level 1.** The waiver and short-sale flags are still reported under the unrevised RTS 22.
4. **Confusing branch reporting with venue reporting.** Branch trades go to the firm's home authority. The host-to-home forwarding rule concerns investment firms' branches, not venues.

<a id="looking-ahead"></a>

## Changes waiting for a revised RTS 22

The 2024 review rewrote Article 26. It adds the effective date, the identity of the entity subject to the reporting obligation and a trading venue transaction identification code, and removes the waiver and short-sale flags. It also changes the scope. OTC derivatives that are in scope only because they are traded on a venue will be reportable only when executed on a venue. The OTC derivatives described in Article 8a(2) will be reportable wherever they are executed. Reports will also go to more authorities. ESMA has said that all these changes take effect only once RTS 22 is revised. In June 2025 ESMA decided not to propose a revised RTS 22 for now and began a wider review of transaction reporting. Its final report of 2 July 2026 recommends some short-term relief and a longer-term single reporting system, but proposes no revised RTS 22. So no date has been set, and the existing standards still apply in practice.

<a id="legal-references"></a>

## Legal references

- [Regulation (EU) No 600/2014 on markets in financial instruments (MiFIR), consolidated version of 23 November 2025](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0600-20251123)

  Article 26 (obligation to report transactions) · Article 27b (ESMA authorisation of data reporting service providers) · Article 27i (ARM requirements)
- [Delegated Regulation (EU) 2017/590 (RTS 22) on the reporting of transactions](https://eur-lex.europa.eu/eli/reg_del/2017/590/oj)

  Annex I (content of transaction reports); not amended since adoption
- [Regulation (EU) 2019/2175 (data reporting services and reference data moved to ESMA)](https://eur-lex.europa.eu/eli/reg/2019/2175/oj)

  ARMs authorised and supervised by ESMA from 1 January 2022
- [ESMA public statement on the transition to the revised MiFIR provisions, 27 March 2024](https://www.esma.europa.eu/sites/default/files/2024-03/ESMA74-2134169708-7163_Public_statement_on_specific_revised_MiFIR_provisions.pdf)

  The amended Article 26 applies only once RTS 22 is revised; until then reporting continues as before
- [ESMA final report on RTS 22 and RTS 24, 23 June 2025](https://www.esma.europa.eu/sites/default/files/2025-06/ESMA12-2121844265-4779_Final_Report_on_RTS_22_and_24.pdf)

  Summarises the consultation feedback; ESMA decided not to propose changes to RTS 22 or RTS 24 for now and began a wider review of transaction reporting
- [ESMA final report on simplifying transaction reporting, 2 July 2026](https://www.esma.europa.eu/sites/default/files/2026-07/ESMA12-1406959660-3235_Final_Report_on_the_Call_for_Evidence_on_a_comprehensive_approach_for_the_simplification_of_financial_transaction_reporting.pdf)

  Recommendations; no revised RTS 22 proposed

<a id="related-h"></a>

## Related topics

Topic 8. **[What order records and instrument reference data does MiFIR require?](order-records-and-reference-data.md)** — Keeping order and transaction records, and sending instrument reference data to ESMA.

Topic 6. **[What must a systematic internaliser quote, and how must it execute client orders?](systematic-internalisers.md)** — Who counts as a systematic internaliser, quoting duties, quote sizes since November 2025 and execution at the quoted price.

Topic 1. **[What does MiFIR cover, and whom does it apply to?](mifir-scope-and-application.md)** — What MiFIR regulates, who it applies to, and how it fits with MiFID II and Law 87(I)/2017.

---

[← Previous topic Systematic internalisers](systematic-internalisers.md) | [Next topic: Records and reference data →](order-records-and-reference-data.md)
