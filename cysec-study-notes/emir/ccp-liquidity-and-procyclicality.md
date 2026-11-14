> [Study notes](../README.md) › [Advanced](../advanced.md) › [EMIR: Derivatives, Clearing and CCPs](README.md) › CCP liquidity  
> Source: <https://www.exampasscy.com/study-notes/emir/ccp-liquidity-and-procyclicality>

CySEC Advanced · Chapter 10 · Topic 6 of 7

# How must a CCP manage liquidity, and how can margins fuel leverage?

How a CCP measures its exposures and liquidity needs, its credit lines and the 25% cap per clearing member group, the liquidity stress scenario since EMIR 3, how margins and haircuts feed leverage cycles, and the rules that dampen procyclicality. · By the [ExamPass CY editorial team](../about.md) · Last reviewed 30 September 2026 · 8 min read

Tested in: Advanced · Ch 10

<a id="short-answer"></a>

## Short answer

A CCP measures its credit and liquidity exposures to each clearing member in **near to real time**, with timely, **non-discriminatory** access to pricing sources at reasonable cost. It must **at all times** have adequate liquidity, backed by credit lines; one clearing member with its parent and subsidiaries may provide at most **25%** of those lines. It measures potential liquidity needs **daily**; since **24 December 2024** the stress assumes the default of at least the **two largest** clearing members **or liquidity providers**. Because margins and haircuts are **procyclical**, EMIR also requires CCPs to limit that effect.

<a id="key-facts"></a>

## CCP liquidity and procyclicality at a glance

| Point | Rule |
| --- | --- |
| Exposure measurement | Credit and liquidity exposures to each clearing member, and to interoperable CCPs, in near to real time |
| Pricing sources | Timely access on a non-discriminatory basis, at reasonable cost |
| Credit lines | Needed for when the CCP cannot use its financial resources immediately; one clearing member, its parent and subsidiaries together provide at most 25% |
| Liquidity needs | Measured daily, assuming the default of at least the two entities with the largest exposures that are clearing members or liquidity providers (not central banks) |
| Liquidity sources | Central bank access, creditworthy and reliable commercial banks, or both; relying on commercial bank lines alone is a risk (recital (71)) |
| Other cover standards | Margins: at least 99% of exposure movements (99.5% for OTC derivatives); default fund: largest member, or second and third together if larger; default fund plus other financial resources: at least the two largest members |
| CCP margin tools | At least one: a 25% buffer, a 25% weight for stressed observations, or a 10-year lookback floor |
| Bilateral margin models | At least 25% of calibration data from a period of significant financial stress |

Source: EMIR, recital (71) and Articles 40, 41, 42, 43, 44 and 46, as amended by Regulation (EU) 2024/2987; Delegated Regulation (EU) No 153/2013, Articles 24, 28 and 32–34; Delegated Regulation (EU) 2016/2251, Article 16.

<a id="in-the-exam"></a>

## In the exam

The exam is written from the exam material, which does not reflect the changes below. Expect its answer. If that answer is not among the options and the current rule is, choose the current rule.

- **Liquidity stress scenario**

  **Exam material:** Each day a CCP measures its potential liquidity needs, assuming that the two clearing members it is most exposed to both default.

  **Current law (since 24 December 2024 (Regulation (EU) 2024/2987, EMIR 3, amending Article 44(1))):** The daily measurement assumes the default of at least the two entities with the largest exposures that are clearing members or liquidity providers, central banks excluded.

<a id="liquidity-rules"></a>

## What liquidity rules must a CCP follow?

A CCP must be able to pay on time even when a clearing member does not. Article 40 requires it to measure and assess its credit and liquidity exposures to every clearing member, and to any CCP it has an interoperability link with, on a near to real-time basis; the exam material words this as near-time or real-time. It needs timely access to the relevant pricing sources, on a non-discriminatory basis and at a reasonable cost, so that it can measure those exposures properly.

Under Article 44 a CCP must always be able to draw on adequate liquidity for its services and activities. It arranges credit lines or similar facilities to cover its needs when the resources at its disposal cannot be used immediately. To avoid dependence on one banking group, the credit lines from any one clearing member, counted together with those from its parent undertaking and subsidiaries, may not exceed 25% of what the CCP needs. The CCP measures its potential liquidity needs every day. The exam material says that measurement assumes that the two clearing members to which the CCP is most exposed default. Since 24 December 2024 EMIR 3 has required the CCP to assume the default of at least the two entities to which it has the largest exposures and that are clearing members or liquidity providers, central banks excluded.

The exam material also says a CCP can draw liquidity from a central bank, from creditworthy and reliable commercial banks, or from both. It adds that a CCP should consider, above all in stressed conditions, the danger of depending on commercial bank credit lines alone. That wording comes from recital (71) of EMIR, which explains the Articles rather than adding a rule of its own. The binding detail is in Delegated Regulation (EU) No 153/2013: a liquidity risk framework with daily monitoring, a list of eligible liquid resources (such as cash, committed credit lines and repos, and highly marketable instruments convertible into cash the same day) and limits on concentration in liquidity providers. The exam material cites Article 41 alongside Article 44 for liquidity; Article 41 in fact governs margins, and Article 40 is the exposure rule.

Terms used in this note

- **Procyclicality** — The tendency of risk requirements to fall in good times and rise in bad times, amplifying the financial cycle.

- **Haircut** — A reduction in the value given to collateral, to allow for a fall in its price before it can be sold.

- **Fire sale** — Forced, rapid selling of assets at depressed prices, often to meet margin calls.

- **Interoperability arrangement** — A link between CCPs that lets participants of one clear trades with participants of another.

<a id="leverage-cycle"></a>

## How can margins and haircuts amplify leverage?

The exam material's text on leverage is a policy explanation rather than a set of EMIR rules. Its point is that collateral requirements which move with the cycle can feed excessive leverage and so create systemic risk, which macroprudential tools aim to contain. Margins and haircuts protect CCPs and bilateral counterparties by absorbing losses, but they can also make the financial cycle swing harder. Two effects combine. When asset prices rise, securities already posted as collateral are worth more, so fewer are needed to secure the same exposure. And because most margin and haircut models are driven by price volatility, requirements fall when markets are calm and rise when volatility jumps.

In a calm, rising market both effects free up collateral, which firms can use to borrow more and to take on larger derivative commitments, building up financial and synthetic leverage. When prices turn, the process reverses: collateral loses value just as margin calls and haircuts increase. Firms that cannot meet the calls must close positions and sell assets quickly, and these fire sales push prices down further, triggering more calls. That is procyclicality: requirements that move with the cycle and amplify it. The exam material presents this as a focus of 'the current revision of EMIR'; the rules in force today include EMIR 3, applicable since 24 December 2024.

<a id="anti-procyclicality"></a>

## Which EMIR rules limit procyclicality?

Under Article 41(1), a CCP's margins must cover losses from at least 99% of exposure movements over an appropriate time horizon, and the CCP must revise them taking account of any procyclical effects of the revisions. For OTC derivatives, Delegated Regulation (EU) No 153/2013 raises the 99% to 99.5%. Since 24 December 2024 the CCP must monitor and revise its margins continuously, not just regularly. Article 28 of Delegated Regulation (EU) No 153/2013 makes the CCP use at least one of three tools: a margin buffer of at least 25% that it may run down when requirements rise sharply; a weight of at least 25% for stressed observations in the lookback period; or a floor equal to margins calculated with volatility over a 10-year lookback. Since 24 December 2024 EMIR itself also requires a CCP revising its haircuts to take account of the need to minimise procyclical effects (Article 46(1)); Delegated Regulation (EU) No 153/2013 already required conservative haircuts that limit procyclicality. EMIR has always required intraday margin calls, at least when set thresholds are exceeded. Since 24 December 2024 the CCP must also consider, as far as possible, how those calls affect participants' liquidity. For uncleared trades, initial margin models under Delegated Regulation (EU) 2016/2251 must draw at least 25% of their data from a period of significant financial stress. How investment firms manage their own liquidity and leverage risk is covered in [What processes must a CIF have for credit, market, liquidity, operational and leverage risk?](../capital-adequacy/managing-specific-risk-types.md)

<a id="how-to-think"></a>

## How to think about it

Separate two questions. Can the CCP pay on time? That is liquidity: exposures tracked in near real time, needs measured daily, credit lines spread across banking groups, and a stress in which at least the two largest members or liquidity providers fail. Can the CCP's own requirements make a crisis worse? That is procyclicality: margins and haircuts that shrink in calm markets and jump in stress. EMIR's answer is buffers, stressed data and long lookbacks, so that requirements move less with the cycle.

<a id="common-mistakes"></a>

## Common mistakes

1. **Using the pre-2024 stress scenario.** Since 24 December 2024 the liquidity stress covers at least the two entities with the largest exposures that are clearing members or liquidity providers, not only clearing members.
2. **Mixing up the CCP's cover standards.** Liquidity stress, and the default fund plus other financial resources: at least the two largest; default fund: the largest, or second and third together; margins: 99%, or 99.5% for OTC derivatives.
3. **Applying the 25% credit-line cap to each bank alone.** The lines from a clearing member, its parent and its subsidiaries are added up and tested together.
4. **Thinking margins rise in booms.** Volatility-based requirements usually fall in calm, rising markets, which is how leverage builds up.

<a id="legal-references"></a>

## Legal references

- [Regulation (EU) No 648/2012 on OTC derivatives, central counterparties and trade repositories (EMIR), consolidated version of 17 January 2025](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02012R0648-20250117)

  Article 40 (exposure management) · Article 41 (margins) · Articles 42 and 43 (default fund and other resources) · Article 44 (liquidity risk controls) · Article 46 (collateral and haircuts)
- [Regulation (EU) No 648/2012 (EMIR), original text as published on 27 July 2012](https://eur-lex.europa.eu/eli/reg/2012/648/oj)

  Recital (71) (sources of CCP liquidity)
- [Regulation (EU) 2024/2987 amending EMIR (EMIR 3)](https://eur-lex.europa.eu/eli/reg/2024/2987/oj)

  Article 1 (new wording of Articles 41, 44 and 46) · Article 5 (application from 24 December 2024)
- [Delegated Regulation (EU) No 153/2013 (requirements for CCPs), consolidated version of 7 March 2024](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02013R0153-20240307)

  Article 24 (margin confidence intervals) · Article 28 (procyclicality) · Articles 32 to 34 (liquidity risk) · Article 41 (haircuts)
- [Delegated Regulation (EU) 2016/2251 (margin for OTC derivatives not cleared by a CCP), consolidated version of 14 February 2023](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02016R2251-20230214)

  Article 16 (calibration of initial margin models)

<a id="related-h"></a>

## Related topics

Topic 5. **[How much capital must a CCP hold, and how do large exposure limits treat CCPs?](ccp-capital-and-large-exposures.md)** — A CCP's minimum and ongoing capital, its skin in the game, and how bank and investment-firm large exposure limits treat exposures to CCPs.

Topic 7. **[What must a CCP disclose, to whom, and when can a breach stay private?](ccp-transparency-and-disclosure.md)** — What a CCP and its clearing members make public, what goes to ESMA and the competent authority, and when a member's breach stays private.

Topic 4. **[How must uncleared OTC derivatives be confirmed, reconciled and collateralised?](emir-risk-mitigation-techniques.md)** — Confirmation, reconciliation, compression and dispute resolution for uncleared trades, daily valuation, and variation and initial margin.

---

[← Previous topic CCP capital](ccp-capital-and-large-exposures.md) | [Next topic: CCP disclosure →](ccp-transparency-and-disclosure.md)
