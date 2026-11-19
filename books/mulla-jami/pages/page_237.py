# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 237 (printed ٢٣٦)."""

PAGE_NUMBER = 237
PRINTED_PAGE = "٢٣٦"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section", "ar": "[التحذير]",
     "en": "Warning (al-Taḥdhīr)"},

    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(الرابع) من تلك المواضع التي وجب حذف ناصب المفعول به فيها (التحذير).",
     "en": "(The fourth) of those places in which the elision of what puts the direct object (mafʿūl bihi) in the accusative is obligatory is (warning—al-taḥdhīr)."},
    {"type": "matn",
     "ar": "وإنما وجب حذف الفعل فيه، لضيق الوقت[[١]] عن ذكره.",
     "en": "The verb must be elided in it only because time is too short to mention it."},
    {"type": "matn",
     "ar": "(وهو) في اللغة: «تخويف شيء عن شيء وتبعيده منه».",
     "en": "(It is), in language: “making something fear something and keeping it far from it.”"},
    # REVIEW: print reads «إصطلاح» with hamza (normally «اصطلاح»); transcribed as printed.
    {"type": "matn",
     "ar": "وفي إصطلاح النحاة: (معمول[[٢]]) أي: اسم عمل فيه النصب بالمفعولية[[٣]] (بتقدير: «اتق»[[٤]] تحذيرا)",
     "en": "In the technical usage of the grammarians: (a governed term—maʿmūl), that is, a noun on which the accusative has operated by virtue of its being an object, (by supplying “ittaqi” [beware], as a warning—taḥdhīran),"},
    {"type": "matn",
     "ar": "أي: حذر ذلك المعمول تحذيرا، فيكون مفعولا مطلقا، أو ذكر تحذيرا، فيكون مفعولا له",
     "en": "that is: “that governed term was warned against with a warning,” so that it is an absolute object (mafʿūl muṭlaq); or “it was mentioned for warning,” so that it is an object of purpose (mafʿūl lahu)"},
    {"type": "matn",
     "ar": "(مما بعده[[٥]]) أي: مما بعد ذلك المعمول (أو ذكر المحذر منه مكررا[[٦]]) على صيغة المجهول عطفا على «حذر» أو «ذكر» المقدر.",
     "en": "(from what follows it), that is, from what follows that governed term; (or [where] the thing warned against is mentioned repeated), “dhukira” being in the passive form and conjoined to the implied “ḥudhdhira” or “dhukira.”"},
    {"type": "matn",
     "ar": "فإن قلت: فعلى هذا لا بد من ضمير في المعطوف كما كان في المعطوف عليه؟",
     "en": "If you say: on this [account], must there not be a pronoun in the conjoined [clause], as there was in the clause conjoined to?"},
    {"type": "matn",
     "ar": "قلنا: نعم[[٧]]، لكنه وضع في المعطوف المظهر موضع المضمر؛",
     "en": "We say: yes; but in the conjoined [clause] the explicit noun has been put in the place of the pronoun;"},
    {"type": "matn",
     "ar": "إذ تقدير الكلام أو معمول بتقدير «اتق» ذكر مكررا، إلا أنه وضع المحذر منه موضع الضمير العائد إلى المعمول إشعارا بأنه محذر منه لا محذر.",
     "en": "for the implied form of the statement is: “or a governed term, by supplying ‘ittaqi,’ that is mentioned repeated”; except that he put “the thing warned against” in place of the pronoun referring to the governed term, to signal that it is what is warned against, not the one warned."},
    {"type": "matn",
     "ar": "(مثل: «إياك والأسد»[[٨]] و«إياك أن تحذف») هذان مثالان لأول نوعي التحذير،",
     "en": "(As in: “Beware of the lion!”—iyyāka wa-l-asada—and “Beware of elision!”—iyyāka an taḥdhifa): these two are examples of the first of the two kinds of warning…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في كلا قسمي التحذير ضيق وقت، وهو أضيق في القسم الثاني منه. ولهذا لا يذكر المحذر منه.",
     "en": "In both kinds of warning time is short, and it is shorter in the second kind; for this reason the thing warned against is not mentioned [separately]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "نقل إليه لتعلق التحذير به لكونه محذرا أو محذرا منه.",
     "en": "[The term] was transferred to it because warning attaches to it, it being either the one warned or the thing warned against."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أشار به إلى أن إطلاق المعمول على اللفظ باعتبار أنه محل لأثر العامل.",
     "en": "By this he indicated that applying “maʿmūl” to the word is on the consideration that it is the locus of the governor’s effect."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الأنسب بالصناعة أن يقال: بـ«اتق» بدون التقدير.",
     "en": "More suited to the technical art would be to say “by ‘ittaqi’” without [the word] “supplying.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هذا القسم الذي هو المحذر: إما ظاهر أو مضمر. والظاهر لا يجيء إلا مضافا إلى المخاطب.",
     "en": "This kind, which is the one warned, is either explicit or a pronoun. The explicit noun comes only annexed to the addressee."},
    {"type": "pair",
     "ar": "والمضمر لا يجيء في الأغلب إلا مخاطبا. وقد يجيء متكلما نحو: إياي والشر.",
     "en": "The pronoun mostly comes only in the second person; it may come in the first person, as in “iyyāya wa-l-sharra” (let me beware of evil)."},
    # REVIEW: print reads «لا حذر» (separated); probably «لأحذر» (let me beware); transcribed as printed.
    {"type": "pair",
     "ar": "وسيبويه يقدر بنحو: لا حذر، وغيره يقدر بنحو حذر خطابا. والأول أولى، كذا ذكره الشيخ الرضي.",
     "en": "Sībawayh supplies [a verb] like “lā ḥadhar” [as printed; probably “la-aḥdhar,” let me beware], and others supply [a verb] like “ḥadhdhir” (warn), in the form of address. The first is preferable; thus Shaykh al-Raḍī stated it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "هذا القسم يكون ظاهرا أو مضمرا سواء كان الظاهر مضافا، أو لا والمضمر متكلما أو مخاطبا أو غائبا.",
     "en": "This kind may be explicit or a pronoun, whether the explicit noun is annexed or not, and the pronoun first, second or third person."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أو قلنا: بتقدير العائد. والتقدير: أو ذكر المحذر منه من نوعيه أو باستتار ضمير في ذكر، وجعل المحذر منه بدلا منه.",
     "en": "Or we say: by supplying the returning pronoun; the implied form being: “or the thing warned against, of its two kinds, is mentioned”; or by a pronoun latent in “dhukira,” with “the thing warned against” made a substitute (badal) for it."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: قال المصنف: الأصل اتقك ثم لما لم يجمعوا بين ضميري الفاعل والمفعول لواحد جاؤوا بالنفس مضافا إلى الكاف، فقالوا: اتق نفسك،",
     "en": "Shaykh al-Raḍī said: the author said: the base form is “ittaqi-ka”; then, since they do not combine the pronouns of agent and object for one referent, they brought “nafs” annexed to the kāf, and said “ittaqi nafsaka” (guard yourself);"},
    {"type": "pair",
     "ar": "فلما حذفوا الفعل حذفوا النفس لعدم الاحتياج إليه، فرجع الكاف، ولم يجز أن يكون متصلا؛ لأن عامله مقدر، فصار منفصلا.",
     "en": "when they elided the verb they elided “nafs,” there being no need for it; so the kāf returned, but it could not be attached, because its governor is implied, and so it became detached [iyyāka]."},
    {"type": "pair",
     "ar": "ثم قال: وأرى أن هذا الذي ارتكبه تطويل مستغنى عنه.",
     "en": "Then he [al-Raḍī] said: I consider what he undertook a needless lengthening."},
    {"type": "pair",
     "ar": "والأولى أن يقال: هو بتقدير إياك بعد بتأخير العامل. وجاز اجتماع ضميري الفاعل والمفعول لواحد إذا كان أحدهما منفصلا.",
     "en": "It is better to say: it is with “iyyāka” implied after, the governor being placed later; and the pronouns of agent and object for one referent may be combined when one of them is detached."},
]
