# The Language Doctrine — Plain Language Is the Law of the Space

**R&D filing RND-20. Online research on how governments write, filed
and enacted as the space's own writing standard. The companion tool is
`plain_lang` (C11, WuBuCore). Connects to GOV-4 (Digital Government
Doctrine). A digital government writes so its people can understand
it.**

---

## Part 1 — The research, filed with sources

### 1.1 Plain language is a law in the United States

The **Plain Writing Act of 2010** (Pub. L. 111-274) makes federal
agencies write "clear Government communication that the public can
understand and use." The act covers the high-stakes writing. That is:
documents needed to get a benefit, meet a rule, or file taxes. That is
exactly the writing a government's people depend on.

Sources: digital.gov/guides/plain-language (GSA);
justice.gov/open/plain-writing-act; congress.gov PLAW-111publ274.

### 1.2 The international definition (the one we adopt)

> "A communication is in plain language if its wording, structure, and
> design are so clear that the intended readers can easily find what
> they need, understand what they find, and use that information."

— **The International Plain Language Federation** (filed verbatim).

Three verbs carry the whole standard: **find, understand, use**. A
filing passes when a first one can find what they need. They can
understand it. They can use it — without help, without a second
reading, without a lawyer.

Source: clarity-international.org/plain-legal-language.

### 1.3 What plain language is NOT (the errors, killed)

- **It is not "dumbed down."** A plain-language legal document is as
  accurate as legalese. Often it is more precise, because it leaves no
  room for ambiguity. (Clarity International)
- **It is not patronizing.** It empowers the reader. Plain legislation
  needs no translation for laypeople. (Clarity International)
- **It is not only for non-experts.** Studies show medium and high
  literacy readers gain the most from plain language. Experts like it
  too. It saves everyone time. (Clarity International; Trudeau 2017,
  U. Arkansas Law Review 40/2)
- **It is not a license to be vague.** Precision and clarity run the
  same direction. The Irish Law Reform Commission confirms plain
  drafting can keep legal certainty.

### 1.4 The writing rules we enact (from digital.gov / GOV.UK)

**Structure:**

1. **Topic sentence first.** Good opening sentences organize the
   writing.
2. **Organize the information.** Prepare readers for what is coming.
   Summarize long documents up front.
3. **Use lists and tables** where they serve the reader. They carry
   detail fast, without overload.
4. **Address the reader as "you,"** not "he," "she," or "the citizen."
   (GOV.UK: "Address the user as 'you' where possible.")

**Voice:**

5. **Active voice, always.** "We file the report." Not "The report is
   filed by us." Passive voice hides who does what. A vigilance space
   can never afford that.

**Words:**

6. **Prefer the short word.** The space bans the corporate lexicon.
   The list is in §1.5. Examples: utilise→use, incentivise→encourage,
   commence→start, robust→well thought out, streamline→simplify,
   facilitate→help, leverage→use, liaise→work with, prior→before,
   subsequent→later, purchase→buy, obtain→get, assist→help,
   additional→more, notwithstanding→even so, initiate→start,
   endeavour→try, ascertain→find out, approximately→about,
   terminate→end, aforementioned→this, heretofore→until now,
   utilization→use. (GOV.UK words-to-avoid, filed)
7. **No metaphors.** "Drive," "leverage," "going forward," "hub,"
   "one-stop shop." Metaphors slow comprehension and hide meaning. Say
   what you actually do. (GOV.UK)
8. **Explain abbreviations on first use.** "WuBu IDentification (WID)"
   once, then WID. (GOV.UK)
9. **No gendered pronouns.** Use "you" and "the first one."

### 1.5 The banned list (the 26 words, filed verbatim)

The full list the checker enforces, with replacements:

| Banned | Use instead | Banned | Use instead |
|---|---|---|---|
| utilise | use | incentivise | encourage |
| utilize | use | commence | start |
| initiate | start | leverage | use |
| liaise | work with | robust | well thought out |
| streamline | simplify | facilitate | help |
| endeavour | try | endeavor | try |
| ascertain | find out | approximately | about |
| subsequent | later | prior | before |
| terminate | end | purchase | buy |
| obtain | get | assist | help |
| additional | more | aforementioned | this |
| notwithstanding | even so | heretofore | until now |
| utilization | use | | |

### 1.6 The measurable standard: Flesch-Kincaid (adopted, with math)

The **Flesch Reading Ease** (Flesch 1948, J. Applied Psychology 32:221)
and **Flesch-Kincaid Grade Level** (Kincaid et al. 1975, U.S. Navy)
are the two formulas in Microsoft Word, Grammarly, and the U.S. Defense
standard. The math, filed exactly:

```
FRES  = 206.835 - 1.015*(words/sentences) - 84.6*(syllables/words)
GRADE = 0.39*(words/sentences) + 11.8*(syllables/words) - 15.59
```

Known anchor values (verified by the C11 tool):

- "The cat sat on the mat." → FRES ≈ 116 (very easy)
- "The Australian platypus is seemingly a hybrid of a mammal and
  reptilian creature." → FRES 37.5, grade 11.3 (documented)
- Reader's Digest ≈ 65; Time ≈ 52; Harvard Law Review ≈ low 30s
  (documented)
- Florida requires insurance at FRES ≥ 45 (documented). The UK
  government sets grade 5 for public documents (documented).

**The WuBu Standard (enacted):** a filing is **CLEAR** when
**FRES ≥ 60** (the "plain English, 13-15 year old" band) **and
grade ≤ 8**. That sits above the insurance floor and below the UK's
strict grade 5. The space writes for its people, not a law library.
But the Bureau files technical documents too. The checker
(`plain_lang`) applies the exact formulas above.

### 1.7 Why it matters to the space (the doctrine's spine)

- **Access to justice is access to the space.** Clarity International:
  "Inaccessible legal writing generates confusion and frustration. It
  can even result in unnecessary charges." A citizen who cannot read
  the law is not governed. They are merely ruled.
- **Trust.** Complexity costs. Siegel+Gale's Global Brand Simplicity
  Index puts the cost at **$98 billion** in wasted effort. The space's
  first asset is trust. Obscurity spends it.
- **Quintilian, filed:** "We should not speak so it is possible for
  the audience to understand us, but so that it is impossible for them
  to misunderstand us." That standard is 1900 years old. Most
  governments still miss it. The space meets it.
- **Vigilance is a reading act.** The Bureau's WBI-1 forms, the Penny
  Clause, the license itself. A first one reads every one of them.
  Obscure writing is the first tool of the thing the Bureau watches.

---

## Part 2 — The doctrine, enacted

### The Language Doctrine (binding on every filing)

1. **Every public filing of the space must pass the WuBu Standard.**
   That means FRES ≥ 60 and grade ≤ 8, measured by `plain_lang`. A
   filing that fails is returned for rewrite. The Bureau does not file
   what its people cannot read.
2. **Active voice is mandatory.** The actor is named. "The Bureau
   files." Not "It is filed."
3. **The banned list is binding.** The 26 words in §1.5 are replaced
   with their plain counterparts. No metaphors. No "utilise."
4. **Address the reader.** Use "you" and "the first one." Never
   "he/she."
5. **The Penny Clause is written in plain language.** The license's
   through-line must be readable by the person holding the penny.
6. **Forms and filings keep the filing voice.** "Filed. Done. Next."
   stays. But the filing voice is plain voice. Bureaucratic whimsy is
   allowed. Bureaucratic obscurity is not.
7. **Every new RND/GOV/ECO/WBI form is checked before filing.** The
   checker is `bin/plain_lang <file>` in WuBuCore. Exit 0 means CLEAR.

### The amendment clause

This doctrine is itself a filing. It is itself measured. If any part
of it reads above grade 8, the amendment is to make it plainer. The
bar does not move. Corrections to over-cautious readings become
doctrine amendments, filed verbatim in the log.

---

*Filed. Done. Next.*
