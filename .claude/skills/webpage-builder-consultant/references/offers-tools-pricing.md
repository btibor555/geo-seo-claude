# Offers, Tools, Value Math, Pricing & Objections

## Opportunity math (always label assumptions)

| Input | Value |
|-------|------:|
| Monthly visitors | V |
| Current conversion rate | c₁ |
| Current leads/month | V × c₁ |
| Target conversion rate | c₂ |
| Target leads/month | V × c₂ |
| Additional leads | V × (c₂ − c₁) |
| Lead → customer close rate | k |
| Average customer value | $A |
| **Monthly opportunity** | V × (c₂ − c₁) × k × A |

Say: *"Based on the numbers you gave me, improving conversion could represent a meaningful
opportunity."* Never: *"I guarantee this will make you $X."*

**Paid ads variant:** cost per lead = spend ÷ leads. If the page converts better, the same
spend buys more leads. Do not promise a specific CPL drop.

## Starter offers

| Offer | Best for | Includes | Price range |
|-------|----------|----------|------------:|
| Conversion Audit | Any site; entry offer | Homepage, mobile, capture, trust, follow-up review + top fixes | Free–$500 |
| Lead Capture Upgrade | Has site, weak capture | CTA cleanup, form, booking, mobile, trust section, CRM, owner alert, confirmation | $1,000–$4,000 |
| One-Page Local Site | No/outdated site | Hero, services, trust, about, FAQ, contact, capture, basic follow-up | $500–$2,000 |
| Campaign Landing Page | Running ads / one offer | Matched headline, CTA, form/booking, proof, FAQ, tracking, follow-up | $750–$3,000 |
| Website + AI Chat | Many questions, slow replies | Page update, AI FAQ chat, qualification, booking, human handoff, CRM | $2,500–$10,000+ |
| Small Business Site | Multi-service | Multi-page, service pages, capture | $2,000–$7,500 |
| Premium Webflow/Framer | Design-critical | Custom design + conversion | $5,000–$15,000+ |
| Monthly Optimization | Post-launch | Testing, tracking, updates, reporting | $300–$2,500/mo |

**Price up when:** more traffic, higher lead value, paid ads, multiple pages, integrations
(CRM/SMS/calendar), copywriting, custom media, tracking, ongoing optimization.
**Price on value, not effort.**

## Tool selection (problem first)

| Business problem | Tool direction |
|------------------|----------------|
| Fast landing page for one offer | v0, Bolt, Framer AI, Manus |
| Simple site that collects leads | Manus, Bolt, Framer AI |
| Client portal / dashboard | Lovable, Manus, Replit |
| Internal tool | Lovable, Replit, Base44 |
| Beautiful marketing page | v0, Framer AI, Bolt |
| Quick proof-of-concept demo | Bolt, Lovable, Manus |
| Already on WordPress | Improve WordPress, don't rebuild |
| Site + CRM + SMS + booking in one (local biz) | GoHighLevel, or AI page → CRM/automation (Zapier/n8n) |
| Paid ads + A/B testing | Unbounce, GoHighLevel, v0/Framer |
| Owner wants to edit it themselves | Wix / Squarespace / Framer |

AI-builder rule: demos and first versions fast; test everything before real customers;
client-owned accounts; no sensitive data unless the stack is appropriate.

## Build prompt template (paste into Manus / Lovable / Bolt / v0)

```
Build a mobile-first, single-page landing page for [BUSINESS], a [INDUSTRY] in [CITY/AREA].
Goal: get visitors to [MAIN ACTION]. Audience: [IDEAL CUSTOMER + PROBLEM].
Sections in order:
1. Hero: headline "[HEADLINE]", sub "[SUB]", primary button "[CTA]", click-to-call [PHONE], trust line "[★ rating · years · license]".
2. Trust strip: [CERTS/BADGES].
3. Services: [SERVICE 1 (money service)], [2], [3] — each 2 lines + CTA.
4. Proof: [REAL REVIEWS — placeholders if not provided, clearly marked].
5. How it works: [3–4 STEPS ending with what happens after submit].
6. Form: fields [FIELDS]; on submit → thank-you page "[EXPECTATION MESSAGE]"; POST to [WEBHOOK/CRM].
7. FAQ: [Q&A list].
8. Contact: NAP, hours, service area [AREAS], map.
Sticky mobile bar with Call + [CTA]. Brand colors [COLORS]. Fast-loading, accessible (WCAG AA), no stock-photo clichés.
Fire analytics events on form submit, call click, and booking. Include privacy policy link [and disclaimers: ...].
Do not invent testimonials, statistics, or credentials.
```

## Objections

| Objection | Response |
|-----------|----------|
| "We already have a website." | The question is whether it helps people understand, trust, contact, book, and get followed up with. |
| "We don't need fancy." | Agreed. Clear, trustworthy, easy to act on beats fancy. |
| "We don't get much traffic." | Then a redesign may not be first — GBP, reviews, ads, outreach first. |
| "I can use Wix myself." | You can. The value is knowing what the page says, what action it drives, and how leads get followed up. |
| "I only care that it looks good." | Design matters only if it supports the goal. We'll do clean design and clear conversion. |
| "Our web company handles it." | Don't duplicate — check whether the site connects to CRM, booking and follow-up. |
| "How do we know it will work?" | Start with one page or one fix, measure visits, leads, bookings for 2–4 weeks, then expand. |

## Pilot KPIs

Visitors · form submissions · calls · bookings · conversion rate · bounce rate · leads in CRM ·
follow-ups completed · speed-to-lead · CPL (if ads) · booked appointments · closed customers.
