# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 583 (printed ٥٨٢)."""

PAGE_NUMBER = 583
PRINTED_PAGE = "٥٨٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the discussion of the particles of incitement from PDF p. 582
    # (the page begins a new sentence).
    {"type": "matn",
     "ar": "فمعناها: إذا دخلت على الماضي التوبيخ واللوم على ترك الفعل.",
     "en": "Their meaning, when they enter upon the past tense, is rebuke and reproach for omitting the act."},
    {"type": "matn",
     "ar": "ومعناها في المضارع: الحض على الفعل، والطلب له.",
     "en": "Their meaning with the imperfect (muḍāriʿ) is urging to the act and requesting it."},
    {"type": "matn",
     "ar": "فهي في المضارع بمعنى الأمر.",
     "en": "So with the imperfect they are in the sense of the imperative."},
    {"type": "matn",
     "ar": "ولا يكون التحضيض في الماضي الذي قد فات إلا أنها تستعمل كثيرا في لوم المخاطب على أنه ترك في الماضي شيئا يمكن تداركه في المستقبل،",
     "en": "Incitement does not apply to a past that has already gone by; but they are often used to reproach the addressee for having omitted in the past something that can be made good in the future;"},
    {"type": "matn",
     "ar": "فكأنها من حيث المعنى للتحضيض على فعل مثل ما فات.",
     "en": "so it is as though, in respect of meaning, they serve to incite to doing the like of what has gone by."},

    {"type": "section", "ar": "[حرف التوقع]",
     "en": "The Particle of Expectation (ḥarf al-tawaqquʿ)"},

    {"type": "matn",
     "ar": "(حرف التوقع والتقريب: «قد») سمي بهما لمجيئه لهما.",
     "en": "(The particle of expectation and approximation: “qad”). It is named after these two because it comes for them."},
    {"type": "matn",
     "ar": "فإن هذا الحرف إذا دخل على الماضي أو المضارع، فلا بد فيها من معنى التحقيق،",
     "en": "For when this particle enters upon the past or the imperfect, the sense of realization (taḥqīq) is indispensable in it;"},
    # REVIEW: «ثم أنه» printed with hamza above the alif (one expects «ثم إنه»); transcribed as printed.
    {"type": "matn",
     "ar": "ثم أنه يضاف في بعض المواضع إلى هذا المعنى في الماضي التقريب من الحال مع التوقع،",
     "en": "then, in some places, there is added to this meaning in the past [tense] approximation to the present, together with expectation;"},
    {"type": "matn",
     "ar": "أي: يكون مصدره متوقعا للمخاطب واقعا عن قريب، كما تقول لمن يتوقع ركوب الأمير: «قد ركب الأمير» أي: حصل عن قريب ما كانت تتوقعه.",
     "en": "that is, its maṣdar is something the addressee expected, having taken place a short while ago; as you say to one who is expecting the emir to ride out: “qad rakiba al-amīr” (the emir has ridden out), that is, what you were expecting has just now come about."},
    {"type": "matn",
     "ar": "ومنه قول المؤذن: «قد قامت الصلاة»، ففيها إذن ثلاثة معان مجتمعة: التحقيق، والتوقع، والتقريب.",
     "en": "Of this kind is the saying of the muezzin: “qad qāmat al-ṣalāh” (the prayer has begun); in it, then, three meanings are combined: realization, expectation and approximation."},
    {"type": "matn",
     "ar": "وقد يكون مع التحقيق التقريب من غير توقع، كما تقول: «قد ركب زيد» لمن لم يتوقع ركوبه.",
     "en": "Approximation may accompany realization without expectation, as when you say “qad rakiba Zaydun” (Zayd has ridden out) to one who did not expect him to ride."},
    {"type": "matn",
     "ar": "(وهي في المضارع) المجرد من ناصب وجازم وحرف تنفيس (للتقليل) أي: يضاف إلى التحقيق في الأغلب التقليل، نحو: «إن الكذوب قد يصدق».",
     "en": "(And with the imperfect), free of a particle governing the subjunctive or the jussive and of a particle of futurity (ḥarf tanfīs), (it is for diminution [taqlīl]), that is, diminution is added to realization in most cases, as in “inna al-kadhūba qad yaṣduqu” (the habitual liar does sometimes tell the truth)."},
    {"type": "matn",
     "ar": "وقد تستعمل للتحقيق مجردا عن معنى التقليل، نحو: ﴿قد نرى تقلب وجهك في السماء﴾[[١]].",
     "en": "It is sometimes used for realization stripped of the sense of diminution, as in “We have certainly seen the turning of your face towards the heaven”."},
    {"type": "matn",
     "ar": "ويجوز الفصل بينها وبين الفعل بالقسم، نحو: «قد -والله- أحسنت»، و«قد لعمري بت ساهرا».",
     "en": "It is permissible to separate it from the verb by an oath, as in “qad — wa-llāhi — aḥsanta” (you have, by Allah, done well) and “qad la-ʿamrī bittu sāhiran” (by my life, I have spent the night awake)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair", "ar": "سورة البقرة: ١٤٤.", "en": "Qurʾān, Sūrat al-Baqara 2:144."},
]
