# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 103 (printed ١٠٢)."""

PAGE_NUMBER = 103
PRINTED_PAGE = "١٠٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "الكلمة بثقل أحد الأمور الثلاثة[[١]] عن الخفة، التي من شأنها أن تعارض ثقل أحد السببين[[٢]]، فتزاحم تأثيره.",
     "en": "…the word out of lightness, by [reason of] the heaviness of one of the three things[[١]] — [a lightness] whose tendency is to oppose the heaviness of one of the two causes[[٢]] and thereby to vie with its effect."},
    {"type": "matn",
     "ar": "وثقل الأولين ظاهر، وكذا العجمة؛ لأن لسان العجم ثقيل على العرب.",
     "en": "The heaviness of the first two is evident, and likewise [that of] non-Arab origin, because the tongue of the non-Arabs is heavy upon the Arabs."},
    {"type": "matn",
     "ar": "(فهند يجوز صرفه) نظرا إلى انتفاء شرط تحتم تأثير التأنيث المعنوي، أعني: أحد الأمور الثلاثة.",
     "en": "(So “Hind” may be fully declined) in view of the absence of the condition for the necessitation of the semantic feminization's effect — I mean: one of the three things."},
    {"type": "matn",
     "ar": "ويجوز عدم صرفه نظرا إلى وجود السببين فيه.",
     "en": "And its non-declension is [also] permissible, in view of the presence of the two causes in it."},
    {"type": "matn",
     "ar": "(وزينب وسقر) علما لطبقة من طبقات النار.",
     "en": "(And “Zaynab” and “Saqar”) — [the latter] as a proper name for one of the levels of the Fire —"},
    {"type": "matn",
     "ar": "(وماه وجور) علمين لبلدتين[[٣]] (ممتنع) صرفها[[٤]].",
     "en": "(and “Māh” and “Jūr”), as proper names of two towns[[٣]] — (their declension is prevented)[[٤]]."},
    {"type": "matn",
     "ar": "أما زينب: فللعلمية والتأنيث المعنوي، مع شرط تحتم تأثيره، وهو الزيادة على الثلاثة.",
     "en": "As for “Zaynab”: [it is prevented] on account of proper-namehood and semantic feminization, together with the condition for the necessitation of its effect — namely, its exceeding three [letters]."},
    {"type": "matn",
     "ar": "وأما سقر: فللعلمية والتأنيث المعنوي، مع شرط تحتم تأثيره، وهو تحرك الأوسط.",
     "en": "As for “Saqar”: on account of proper-namehood and semantic feminization, together with the condition for the necessitation of its effect — namely, the vowelling of the middle [letter]."},
    {"type": "matn",
     "ar": "وأما ماه وجور: فللعلمية والتأنيث المعنوي مع شرط تحتم تأثيره، وهو العجمة.",
     "en": "As for “Māh” and “Jūr”: on account of proper-namehood and semantic feminization, together with the condition for the necessitation of its effect — namely, non-Arab origin."},
    {"type": "matn",
     "ar": "(فإن[[٥]] سمي به) أي: بالمؤنث المعنوي (مذكر، فشرطه) في سببية منع الصرف (الزيادة على الثلاثة[[٦]])؛",
     "en": "(“So if a masculine [entity] is named[[٥]] with it”) — that is, with the semantically feminine [word] — (“then its condition,”) with respect to [its] being a cause of preventing declension, is (“the exceeding of three [letters]”[[٦]]);"},
    {"type": "matn",
     "ar": "لأن الحرف الرابع في حكم تاء التأنيث قائم مقامها.",
     "en": "because the fourth letter stands in the ruling of the feminine tāʾ, taking its place."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إن قلت: هذا الثقل يوجب تحتم تأثير كل من العلمية والتأنيث، وتحتم تأثير كليهما، فلم جعله المصنف موجبا لتحتم تأثير التأنيث؟",
     "en": "If you say: this heaviness necessitates the necessitation of the effect of both proper-namehood and feminization [severally], and the necessitation of the effect of the two together — so why did the author make it necessitate [specifically] the necessitation of feminization's effect?"},
    {"type": "pair",
     "ar": "قلنا: لأن الكلام مسوق لبيان شرط التأنيث، أو لأن المحتاج إلى التقوية، هو التأنيث، لكونه معنويا دون العلمية، وفي الأخير بحث؛ لأنه لا يلائم البيان الذي ذكره الشارح.",
     "en": "We say: because the discourse is set forth to explain the condition of feminization; or because what needs strengthening is feminization — it being semantic — rather than proper-namehood. But there is a difficulty in this last [point], because it does not accord with the exposition that the commentator gave."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يفهم من هذا الكلام أن أسباب منع الصرف لا يخلو عن ثقل، وهذا غير ظاهر في العدل والوصف والمعرفة، وليس الثقل أمرا اعتباريا حتى يتحقق باعتبار المعتبر.",
     "en": "It is understood from this statement that the causes of preventing declension are not free of heaviness; but this is not evident in the cases of deflection (al-ʿadl), adjectivity, and definiteness — and heaviness is not a merely notional matter such that it could be realized by the consideration of one who considers it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أشار بقوله: لبلدتين إلى وجه تأنيث العلمين. اعلم أن أسماء الأماكن قد يلتزم تأنيثها بتأويل البلدة مثلا، فيمتنع صرفها، وقد يلتزم تذكيرها بتأويل المكان مثلا فتصرف. وقد يعتبر كل منهما فجاز الوجهان.",
     "en": "By his words “of two towns” he indicated the basis for the feminine gender of the two proper names. Know that the names of places are sometimes consistently treated as feminine — by construing [them] as “the town (al-balda),” for instance — so their declension is prevented; and sometimes consistently treated as masculine — by construing [them] as “the place (al-makān),” for instance — so they are declined; and sometimes each [construal] is admitted, so both ways are permissible."},
    {"type": "pair",
     "ar": "إذا عرفت هذا فنقول: إن كان الاستعمال معلوما فذلك، وإن لم يكن معلوما فلك فيه الوجهان. وكذا أسماء القبائل في تأويلها بالقبيلة والحي.",
     "en": "Once you have grasped this, we say: if the [attested] usage is known, then [follow] that; and if it is not known, both ways are open to you. The same holds for the names of tribes, in construing them as “the tribe (al-qabīla)” or “the clan (al-ḥayy).”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أو ممتنع كل منها عن الصرف. والأول أوفق بقوله: يجوز.",
     "en": "Or: each of them is prevented from declension. But the first [reading] accords better with his words “may [be declined].”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الفاء للتفصيل.",
     "en": "The fāʾ is for [introducing] the detailed exposition (tafṣīl)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قال عبد الغفور: وههنا شروط تركها. أحدها: ألا يكون ذلك المؤنث مذكرا بحسب الأصل،",
     "en": "ʿAbd al-Ghafūr said: here there are [further] conditions that he omitted. The first: that the feminine [word] in question not be masculine in origin;"},
    {"type": "pair",
     "ar": "فالمؤنث الذي كان منقولا عن مذكر إذا سمي به مذكر صرف، وكذا حائض، فإنه في الأصل لمذكر، وهو الشخص؛ لأن الأصل في الصفات أن يكون المجرد عن التاء منها صيغة المذكر.",
     "en": "So a feminine [word] that was transferred from a masculine, when a masculine is named with it, is fully declined; and likewise “ḥāʾiḍ” (menstruating), for it is in origin for a masculine — namely “the person (al-shakhṣ)” — because the default in adjectives is that the form stripped of the tāʾ is the masculine form."},
    {"type": "pair",
     "ar": "وثانيها: ألا يكون تأنيثه محتاجا إلى تأويل غير لازم كرجال، فإن تأنيثه بتأويل الجماعة، وهو غير لازم لجواز تأويله",
     "en": "The second: that its feminine gender not depend on a non-necessary construal — like “rijāl” (men), for its feminine gender is by construing [it] as “the group (al-jamāʿa),” which is not necessary, since it may [also] be construed…"},  # continues on the next page
]
