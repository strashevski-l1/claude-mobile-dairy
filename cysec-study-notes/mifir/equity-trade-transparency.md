> [Study notes](../README.md) › [Advanced](../advanced.md) › [MiFIR: Transparency, Reporting and Derivatives](README.md) › Equity transparency  
> Source: <https://www.exampasscy.com/study-notes/mifir/equity-trade-transparency>

CySEC Advanced · Chapter 8 · Topic 2 of 9

# What must trading venues publish before and after trades in shares and ETFs?

Which instruments count as equity, the quotes and depth venues must show before trading, post-trade publication of price, volume and time, deferred publication with CySEC's approval, and the liquid-market test for shares. · By the [ExamPass CY editorial team](../about.md) · Last reviewed 30 September 2026 · 7 min read

Tested in: Advanced · Ch 8, Basic · Ch 4

<a id="short-answer"></a>

## Short answer

For transparency, **equity** instruments are shares, depositary receipts, **ETFs**, certificates and similar instruments. Before trading, a venue publishes **current bid and offer prices** and the **depth of trading interest** at each price, **continuously during normal trading hours**, calibrated for order-book, periodic auction, quote-driven and hybrid systems. After trading, it publishes the **price, volume and time** of each transaction as close to real time as technically possible. **CySEC** may authorise deferred publication, mainly for **large-in-scale** trades, and the venue must disclose the arrangements.

<a id="key-facts"></a>

## Equity transparency at a glance

| Point | Rule |
| --- | --- |
| Equity instruments | Shares, depositary receipts, ETFs, certificates and other similar financial instruments |
| Non-equity instruments | Bonds, derivatives, structured finance products and emission allowances |
| Pre-trade content | Current bid and offer prices and the depth of trading interest at each price, including actionable indications of interest |
| When | Continuously during normal trading hours |
| Trading systems | Order-book, periodic auction, quote-driven and hybrid systems; voice trading is not one of them for equity |
| Access to publication arrangements | On reasonable commercial terms and without discrimination, for systematic internalisers (pre-trade) and firms publishing their OTC trades (post-trade) |
| Post-trade | Price, volume and time of each transaction, as close to real time as technically possible |
| Deferred publication | Only with CySEC's prior authorisation, based on type or size, in particular large in scale; arrangements disclosed to market participants and the public |
| Market data | Pre-trade and post-trade data offered separately, on a reasonable commercial basis, and free of charge 15 minutes after publication |
| Liquid share (since 2 March 2026) | All three, for a share traded daily: market capitalisation of at least €100 million, an average of at least 250 trades a day, average daily turnover of at least €1 million. If fewer than five shares first admitted in a Member State pass, the competent authority may designate others as liquid, up to five |

Source: MiFIR, Articles 3, 6, 7, 12 and 13; Delegated Regulation (EU) 2017/567, Article 1, as amended by Delegated Regulation (EU) 2026/482.

<a id="equity-or-not"></a>

## Which instruments count as equity for transparency?

MiFIR has two transparency regimes, one for equity and one for non-equity instruments, so the first step is always to sort the instrument. Equity instruments are shares, exchange-traded funds (ETFs), depositary receipts, certificates and other similar financial instruments. Non-equity instruments are bonds, derivatives, structured finance products and emission allowances, covered in [What transparency applies to bonds, derivatives and other non-equity instruments?](non-equity-trade-transparency.md) The duties in this note fall on market operators and investment firms that operate a trading venue. For shares and other equity instruments, that means a regulated market or an MTF, because an OTF cannot trade them. How venues admit instruments and members, and control algorithmic trading and direct electronic access, is covered in [How do regulated markets admit instruments and members, and control algorithmic trading?](../cypriot-investment-firms/regulated-market-trading-rules.md)

Several equity rules depend on whether a share has a liquid market. Since 2 March 2026 a share traded daily has a liquid market if it passes all three tests: a market capitalisation of at least €100 million, an average of at least 250 trades a day, and an average daily turnover of at least €1 million. The capitalisation test replaced the former free-float test. If fewer than five shares first admitted in a Member State pass, the competent authority may treat others as liquid, up to five in total. Liquidity matters for the negotiated-trade waiver and for systematic internalisers, which publish quotes only in liquid shares (see [What must a systematic internaliser quote, and how must it execute client orders?](systematic-internalisers.md)).

Terms used in this note

- **Pre-trade transparency** — Publishing bid and offer prices and the depth of interest before trades take place.

- **Post-trade transparency** — Publishing the price, volume and time of trades once they are executed.

- **Depth of trading interest** — How much volume buyers and sellers have entered at each quoted price.

- **Large in scale** — An order or trade that is big compared with normal market size for the instrument; it may qualify for a waiver or a deferral.

<a id="pre-trade"></a>

## What must a venue show before a trade?

Under Article 3(1), a venue makes public the current bid and offer prices for the shares and other equity instruments traded on it, and the depth of trading interest at each price. Actionable indications of interest count too. The information must be available to the public continuously during normal trading hours.

The requirement is calibrated to the type of trading system. MiFIR names four for equity: order-book systems, periodic auctions, quote-driven systems and hybrid systems. Voice trading is not on the equity list. The exam material's non-equity rules add voice trading systems to the list. Since 28 March 2024 that difference no longer holds, because non-equity pre-trade transparency now applies only to central limit order book and periodic auction systems. The venue must also give systematic internalisers, which publish their own quotes, access to the arrangements it uses to publish this information, on reasonable commercial terms and without discrimination. A venue may be allowed not to publish under the waivers explained in [When can a venue trade shares without pre-trade transparency?](equity-pre-trade-waivers.md)

<a id="post-trade"></a>

## What must a venue publish after a trade, and when can it wait?

After execution, the venue publishes the price, volume and time of each transaction in equity instruments, as close to real time as technically possible (Article 6). Investment firms that must publish their own OTC trades under Article 20 can use the venue's publication arrangements; access must be on reasonable commercial terms and must not discriminate. Pre-trade and post-trade data must be offered separately. Market data must be sold on a reasonable commercial basis and made free of charge 15 minutes after publication; the details, and the rules for APAs and consolidated tapes, are in [What are APAs, ARMs and CTPs, and who supervises them today?](../cypriot-investment-firms/data-reporting-service-providers.md)

Publication may be delayed only with CySEC's authorisation. Under Article 7, CySEC may allow a venue to defer publication based on the type or size of the transaction, in particular trades that are large in scale compared with normal market size. The venue needs CySEC's prior approval of its proposed arrangements and must clearly disclose them to market participants and the public. ESMA monitors how deferrals are used and reports to the European Commission every year. If another Member State's authority disagrees with a deferral that CySEC has authorised, it may refer the matter to ESMA. The 2024 review did not change these equity deferral rules. For bonds, structured finance products and emission allowances, by contrast, deferrals have not needed CySEC's authorisation since 2 March 2026.

<a id="how-to-think"></a>

## How to think about it

Work through three questions. Is the instrument equity (shares, depositary receipts, ETFs, certificates) or non-equity? Is the information pre-trade (quotes and depth, shown continuously in normal hours) or post-trade (price, volume and time, close to real time)? Is there a lawful reason not to publish now: a waiver for pre-trade, or a CySEC-authorised deferral for post-trade? For equity, the answer to the last question always involves CySEC, whether it grants a waiver after notifying ESMA or authorises a deferral.

<a id="common-mistakes"></a>

## Common mistakes

1. **Thinking a waiver also removes post-trade publication.** Waivers concern only pre-trade information. Executed trades are still published, subject to any authorised deferral.
2. **Assuming a venue can delay post-trade publication on its own.** For equity, deferral needs CySEC's prior authorisation, and the arrangements must be disclosed.
3. **Assuming the 2024 review changed equity deferrals.** It did not. Equity deferrals still need CySEC's prior authorisation. Only non-equity deferrals were harmonised: for bonds, structured finance products and emission allowances since 2 March 2026, with derivatives to follow.
4. **Relying on the old free-float test for liquid shares.** Since 2 March 2026 market capitalisation replaces it, alongside the trade-count and turnover tests.

<a id="legal-references"></a>

## Legal references

- [Regulation (EU) No 600/2014 on markets in financial instruments (MiFIR), consolidated version of 23 November 2025](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0600-20251123)

  Article 3 (pre-trade transparency, equity) · Article 6 (post-trade transparency) · Article 7 (deferred publication) · Articles 12–13 (separate data, reasonable commercial basis)
- [Delegated Regulation (EU) 2026/482 amending Delegated Regulation (EU) 2017/567](https://eur-lex.europa.eu/eli/reg_del/2026/482/oj)

  Article 1 of Delegated Regulation (EU) 2017/567 (liquid market for shares), from 2 March 2026

<a id="related-h"></a>

## Related topics

Topic 3. **[When can a venue trade shares without pre-trade transparency?](equity-pre-trade-waivers.md)** — The four pre-trade waivers for equity, ESMA's opinion and when CySEC withdraws a waiver.

Topic 4. **[How does the volume cap limit dark trading under equity waivers?](volume-cap-on-waiver-trading.md)** — The single 7% EU-wide cap on trading under the reference price waiver, and the old double volume cap.

Topic 6. **[What must a systematic internaliser quote, and how must it execute client orders?](systematic-internalisers.md)** — Who counts as a systematic internaliser, quoting duties, quote sizes since November 2025 and execution at the quoted price.

---

[← Previous topic Scope of MiFIR](mifir-scope-and-application.md) | [Next topic: Equity waivers →](equity-pre-trade-waivers.md)
