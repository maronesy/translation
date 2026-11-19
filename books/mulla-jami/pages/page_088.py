# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 88 (printed ٨٧).

The two secondarinesses of the verb, and why each ground preventing declension
entails a secondariness. The first footnote block continues footnote 8 of the
previous page.
"""

PAGE_NUMBER = 88
PRINTED_PAGE = "٨٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "إحداهما: افتقاره إلى الفاعل.",
     "en": "The first of the two [secondarinesses of the verb] is its need for a subject (fāʿil)."},
    {"type": "matn",
     "ar": "وأخراهما: اشتقاقه من المصدر.",
     "en": "The second of them is its being derived from the verbal noun (maṣdar)."},
    {"type": "matn",
     "ar": "فمنع منه الإعراب[[١]] المختص بالاسم، وهو الجر والتنوين، الذي هو علامة التمكن.",
     "en": "So there is withheld from it [the diptote] the inflection proper to the noun — namely the genitive [kasra] and the tanwīn — which is the sign of full [nominal] establishment (tamakkun)."},
    {"type": "matn",
     "ar": "وإنما قلنا: إن لكل علة فرعية:",
     "en": "We said “every cause [entails] a secondariness” only [for the following reasons]:"},
    {"type": "matn",
     "ar": "لأن العدل فرع المعدول عنه[[٢]].",
     "en": "because the deviated form (al-ʿadl) is secondary to that from which it deviated (al-maʿdūl ʿanhu);"},
    {"type": "matn",
     "ar": "والوصف فرع الموصوف[[٣]].",
     "en": "and the attribute (al-waṣf) is secondary to the thing qualified (al-mawṣūf);"},
    {"type": "matn",
     "ar": "والتأنيث فرع التذكير؛ لأنك تقول: «قائم»[[٤]]، ثم تقول: «قائمة».",
     "en": "and the feminine (al-taʾnīth) is secondary to the masculine (al-tadhkīr), for you say “qāʾim” (m.) and then you say “qāʾima” (f.);"},
    {"type": "matn",
     "ar": "والتعريف فرع التنكير؛ لأنك تقول: «رجل»، ثم تقول: «الرجل»[[٥]].",
     "en": "and definiteness (al-taʿrīf) is secondary to indefiniteness (al-tankīr), for you say “rajul” (a man) and then you say “al-rajul” (the man);"},
    {"type": "matn",
     "ar": "والعجمة في كلام العرب فرع العربية؛ إذ الأصل في كل كلام ألا يخالطه لسان آخر.",
     "en": "and foreignness (al-ʿujma) within the speech of the Arabs is secondary to Arabicness, since the default in any language is that no other tongue be mixed into it."},

    {"type": "rule"},

    # ---------------- Continuation of footnote 8 from the previous page ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "الفاعل يعطى عمله، ولا يبنى لضعف أمر الفعل في البناء. ولذا يعرب المضارع بتطفله على الاسم.",
     "en": "…the active participle (ism al-fāʿil) — it is given its [the verb’s] governing power, yet it is not made indeclinable, because the verb’s standing with respect to indeclinability is weak. That is why the imperfect verb is [itself] inflected, through its parasitic dependence on the noun."},
    {"type": "pair",
     "ar": "وإذا شابهه بوجه بعيد ككونه فرعا، فلا يبنى بهذه المشابهة لضعفها مع ضعف الفعل في البناء، ولا يعطى بها عمل الفعل لخلوه من المعنى الفعلي، بل ينزع بها علامة الإعراب، وهو التنوين، ثم يتبعه الكسر، أو ينزعان معا.",
     "en": "And when [a noun] resembles it [the verb] in a remote respect — such as its being secondary — it is not made indeclinable by this resemblance, because of the weakness of that [resemblance] together with the verb’s weakness regarding indeclinability; nor is it given the verb’s governance thereby, since it is devoid of verbal meaning; rather, by [this resemblance] the sign of inflection — the tanwīn — is stripped from it, and then the kasra follows suit, or the two are stripped away together."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وفي تقديم الكسرة على التنوين إشارة إلى ذلك، أو منع التنوين أولا، ثم أتبع الكسرة. وقد جوز المصنف الأمرين في (الإيضاح).",
     "en": "In placing “the kasra” before “the tanwīn” [in the phrase “no kasra and no tanwīn”] there is an indication of that [ordering], or [it means] that the tanwīn is barred first and then the kasra made to follow. The author permitted both [orderings] in al-Īḍāḥ."},
    {"type": "pair",
     "ar": "ومال الشيخ الرضي إلى الثاني بعود الكسرة بضرورة عود التنوين، وعدم ضرورة عودها.",
     "en": "Shaykh al-Raḍī inclined to the second [view], [holding] that the return of the kasra follows necessarily from the return of the tanwīn, whereas its own [independent] return is not necessary."},
    {"type": "pair",
     "ar": "وإنما أتبع الكسر التنوين؛ لأن التنوين يحذف لا لمنع الصرف أيضا كما في الوقف واللام والإضافة، فأرادوا النص من أول الأمر على أنه لم يسقط إلا لمشابهته الفعل، فحذفوا صورة الكسر التي لا تدخل الفعل.",
     "en": "The kasra follows the tanwīn only because the tanwīn is [also] dropped for a reason other than the prevention of declension — as in pause (waqf), with the definite article (lām), and in the genitive construction (iḍāfa) — so they wished to make explicit from the outset that it [the tanwīn] drops only on account of its resemblance to the verb; hence they dropped the form of the kasra, which does not occur in the verb."},
    {"type": "pair",
     "ar": "وقال المصنف: إنما يتبعه؛ لأن الكسر يلازم التنوين، فإذا انتفى التنوين من غير عوض انتفى الكسر أيضا؛ لأنه يلازمه.",
     "en": "The author said: it follows it only because the kasra necessarily accompanies the tanwīn; so when the tanwīn is negated without a substitute, the kasra too is negated, because it accompanies it."},
    {"type": "pair",
     "ar": "وإنما قال: من غير عوض؛ إذ لو انتفى التنوين مع العوض، وهو اللام أو الإضافة، لم ينتف الكسر؛ لأن وجود العوض وجود المعوض.",
     "en": "He said “without a substitute” only because, were the tanwīn negated together with the substitute — which is the lām or the iḍāfa — the kasra would not be negated; for the presence of the substitute [counts as] the presence of that for which it substitutes."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأن الأصل بقاء الاسم على حاله.",
     "en": "Because the default is that the noun remains in its [original] state."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لتوقف معناه على ما يقوم به.",
     "en": "Because its meaning depends upon that in which it inheres (mā yaqūmu bihi)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فهو فرع له لفظا. ولما غلب المذكر على المؤنث كان فرعا له في المعنى، هكذا قالوه.",
     "en": "So it is secondary to it verbally (lafẓan). And since the masculine predominates over the feminine, [the feminine] is [also] secondary to it in meaning — thus they have stated it."},
    {"type": "pair",
     "ar": "وفيه بحث؛ لأن التأنيث طار على «قائم» مطلقا لا على «قائم» من حيث هو مجرد عن التاء، والمذكر هو هذا لا ذاك، فإنه المشترك بين المذكر والمؤنث.",
     "en": "But there is [room for] discussion in this: for feminization supervenes upon “qāʾim” absolutely, not upon “qāʾim” considered as stripped of the tāʾ; whereas the masculine is this [latter, the bare form], not that [former] — for it [the bare form] is what is common to both the masculine and the feminine."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني أن التعريف طار على التنكير غالبا إما بوضع جديد أو بأداة، فهو فرع له لفظا.",
     "en": "That is: definiteness generally supervenes upon indefiniteness, either by a fresh coinage or by an instrument [e.g. the article], so it is secondary to it verbally."},
    {"type": "pair",
     "ar": "ولما كان ما يعرفه كان مجهولا لنا كان التعريف فرعا للتنكير معنى.",
     "en": "And since that which one makes definite had been unknown to us [beforehand], definiteness is [also] secondary to indefiniteness in meaning."},
]
