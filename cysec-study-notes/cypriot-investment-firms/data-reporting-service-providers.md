> [Study notes](../README.md) › [Advanced](../advanced.md) › [Cypriot Investment Firms (CIFs)](README.md) › Data reporting service providers  
> Source: <https://www.exampasscy.com/study-notes/cypriot-investment-firms/data-reporting-service-providers>

CySEC Advanced · Chapter 2 · Topic 10 of 10

# What are APAs, ARMs and CTPs, and who supervises them today?

The three data reporting services, what each must publish or report and how fast, the reasonable commercial basis rules for market data, and the move of supervision to ESMA. · By the [ExamPass CY editorial team](../about.md) · Last reviewed 30 September 2026 · 6 min read

Tested in: Advanced · Ch 2, Basic · Ch 2

<a id="short-answer"></a>

## Short answer

Data reporting service providers publish or report trade data for the market. An **APA** publishes investment firms' trade reports, an **ARM** sends transaction reports to regulators by the **close of the next working day**, and a **CTP** consolidates market data from trading venues and APAs. The exam material has CySEC authorising them; since **1 January 2022** **ESMA** has authorised and supervised them, except small APAs and ARMs with a derogation. Market data must be sold on a **reasonable commercial basis**, with **90 days'** notice of fee changes.

<a id="key-facts"></a>

## DRSPs at a glance

| Point | Rule |
| --- | --- |
| APA | Publishes trade reports on behalf of investment firms as close to real time as technically possible |
| ARM | Reports transaction details to authorities as quickly as possible and no later than the end of the next working day; checks reports and has errors corrected |
| CTP | Collects market data from trading venues and APAs and consolidates it into one continuous live data stream |
| Supervisor | ESMA since 1 January 2022; national authorities only for APAs and ARMs with a derogation |
| What is published | At least instrument identifier, price, volume, time of trade, time reported, price notation, venue or SI/OTC code and any special flags |
| Reasonable commercial basis | Cost-based fees with a reasonable margin, non-discriminatory access, the same margin within each client category, each provision charged only once, no bundling, a published data policy, 90 days' notice of changes |
| Free data | Trading venues, APAs and systematic internalisers free after 15 minutes; since 28 March 2024 CTPs give free access to retail investors, academics, civil society and authorities instead |

Source: Regulation (EU) No 600/2014, Title IVa and Article 13, as amended by Regulations (EU) 2019/2175 and 2024/791; Delegated Regulation (EU) 2025/1156.

<a id="in-the-exam"></a>

## In the exam

The exam is written from the exam material, which does not reflect the changes below. Expect its answer. If that answer is not among the options and the current rule is, choose the current rule.

- **Who authorises DRSPs**

  **Exam material:** CySEC authorises data reporting service providers whose home state is Cyprus and keeps them on its public register.

  **Current law (since 1 January 2022 (Regulation (EU) 2019/2175)):** ESMA authorises and supervises APAs, ARMs and CTPs. National authorities, CySEC in Cyprus, keep only APAs and ARMs that qualify for a derogation.
- **Free data from CTPs**

  **Exam material:** CTPs make the data free of charge 15 minutes after publication.

  **Current law (since 28 March 2024 (Regulation (EU) 2024/791, the MiFIR review)):** The 15-minute rule binds trading venues, APAs and systematic internalisers. CTPs instead give free access to retail investors, academics, civil society organisations and supervisors.

<a id="three-services"></a>

## What does each data reporting service do?

An approved publication arrangement (APA) publishes trade reports on behalf of investment firms, meeting their post-trade transparency duties. For each trade it makes public at least the instrument identifier, the price, the volume, the time of the trade and the time it was reported, the price notation, the code of the venue (or SI or OTC where the trade was off-venue) and any special conditions, as close to real time as technically possible.

An approved reporting mechanism (ARM) sends transaction reports to the authorities on behalf of investment firms, as quickly as possible and no later than the close of the working day after the transaction. It must check that reports are complete, catch gaps and obvious mistakes made by the firm, tell the firm and ask it to resubmit; mistakes the ARM itself causes, it corrects and resends. A consolidated tape provider (CTP) collects market data from trading venues (regulated markets, MTFs and OTFs) and APAs and combines it into a single continuous electronic live data stream; since the 2024 MiFIR review the tape for shares and ETFs carries the best bid and offer as well as completed trades.

All three need a management body with the collective knowledge, skills and experience to understand the business, arrangements to prevent conflicts of interest, and sound security to protect the data and prevent unauthorised access.

Terms used in this note

- **APA** — Approved publication arrangement: publishes trade reports on behalf of investment firms.

- **ARM** — Approved reporting mechanism: reports transaction details to the authorities on behalf of investment firms.

- **CTP** — Consolidated tape provider: consolidates market data from trading venues and APAs into one continuous live stream, with one provider per asset class.

- **Reasonable commercial basis** — The EU rules on pricing market data: cost-based, non-discriminatory, charged only once, unbundled and transparent.

<a id="who-supervises"></a>

## Who authorises and supervises them now?

The exam material describes DRSPs being authorised by CySEC and kept on its public register. That changed on 1 January 2022, when Regulation (EU) 2019/2175 moved authorisation and supervision of APAs, ARMs and CTPs to ESMA. National authorities kept only APAs and ARMs that qualify for a derogation because of their limited size and reach, and in Cyprus the provisions of Law 87 on DRSPs were deleted in 2021.

The MiFIR review of 2024, Regulation (EU) 2024/791, went further for CTPs: ESMA selects one consolidated tape provider per asset class through a tender. In July 2026 ESMA authorised the first CTP, for shares and exchange-traded funds, with a transition period until 30 September 2026 to prepare the start of its service.

<a id="market-data-pricing"></a>

## How must market data be priced and made available?

APAs and CTPs, like trading venues and systematic internalisers, must make market data available on a reasonable commercial basis. Fees reflect what it costs to produce and distribute the data, plus a reasonable margin, and access must be non-discriminatory. Fees may differ only between client categories set on factual, easily verifiable criteria, with the same margin for every client in a category and each client in one category only. Each provision of data is charged only once, and data is not bundled with other services. The exam material describes the earlier version of these rules, with fees per end user, prices set by level of disaggregation and differences proportionate to the value of the data.

Each provider publishes a market data policy with its fee schedules, client categories, terms and cost methodology, and must give clients at least 90 days' notice of any unilateral change to fees or terms; a client facing less favourable terms may withdraw. These rules sit in MiFIR Article 13 and Delegated Regulation (EU) 2025/1156, which has applied to existing providers since 23 August 2026. Trading venues, APAs and systematic internalisers must also make data free of charge 15 minutes after publication. The exam material applies that 15-minute rule to CTPs too; since 28 March 2024 CTPs instead give free access to retail investors, academics, civil society organisations and supervisors.

<a id="how-to-think"></a>

## How to think about it

Match each provider to its audience. The APA speaks to the market by publishing trades, the ARM speaks to the regulator by reporting transactions by the next working day, and the CTP puts the whole market's trades on one screen. Remember the supervisor has changed to ESMA, and remember the pricing formula: cost plus a reasonable margin, the same margin within a client category, charged only once, unbundled, and 90 days' warning before fees change.

<a id="common-mistakes"></a>

## Common mistakes

1. **Swapping the roles of APAs and ARMs.** APAs publish trades to the market; ARMs report transactions to authorities.
2. **Giving ARMs a same-day deadline.** They report no later than the close of the following working day.
3. **Naming CySEC as today's supervisor of DRSPs.** ESMA has supervised them since 1 January 2022, except derogated APAs and ARMs.
4. **Allowing different margins within the same client category.** Fees may differ only between categories, with the same margin for every client in a category.

<a id="legal-references"></a>

## Legal references

- [Regulation (EU) No 600/2014 on markets in financial instruments (MiFIR), as amended](https://eur-lex.europa.eu/eli/reg/2014/600/oj)

  Article 13 (reasonable commercial basis) · Title IVa, Articles 27a–27i (data reporting services)
- [Regulation (EU) 2019/2175 (transfer of DRSP authorisation and supervision to ESMA)](https://eur-lex.europa.eu/eli/reg/2019/2175/oj)
- [Regulation (EU) 2024/791 amending MiFIR (MiFIR review)](https://eur-lex.europa.eu/eli/reg/2024/791/oj)
- [Commission Delegated Regulation (EU) 2025/1156 on making market data available on a reasonable commercial basis](https://eur-lex.europa.eu/eli/reg_del/2025/1156/oj)

<a id="related-h"></a>

## Related topics

Topic 9. **[How do regulated markets admit instruments and members, and control algorithmic trading?](regulated-market-trading-rules.md)** — Admitting instruments and members, monitoring trading, direct electronic access and controls on algorithms.

Topic 8. **[How is a regulated market authorised and supervised, and when must it alert CySEC?](regulated-market-authorisation.md)** — Authorising a regulated market and its operator, owners with significant influence, and the signals operators report to CySEC.

Topic 7. **[What is an SME growth market, and how does an MTF qualify?](sme-growth-markets.md)** — Which issuers count as SMEs, the 50% test for an SME growth market, and when the status is lost.

---

[← Previous topic Regulated markets: trading rules](regulated-market-trading-rules.md) | [Chapter overview: Cypriot Investment Firms (CIFs) →](README.md)
