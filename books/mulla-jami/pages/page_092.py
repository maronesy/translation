# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 92 (printed ٩١)."""

PAGE_NUMBER = 92
PRINTED_PAGE = "٩١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "لزومهما للكلمة بمنزلة تأنيث آخر، فصار التأنيث مكررا، بخلاف التاء، فإنها ليست لازمة للكلمة[[١]]، بحسب أصل الوضع،",
     "en": "The inseparability of the two of them from the word is tantamount to a further feminization, so the feminization became reduplicated — unlike the tāʾ [of feminization], for it is not inseparable from the word according to the original coinage,"},

    {"type": "matn",
     "ar": "فإنها وضعت فارقة بين المذكر والمؤنث،",
     "en": "for it [the tāʾ] was coined as a distinguisher between the masculine and the feminine,"},

    {"type": "matn",
     "ar": "فلو عرض اللزوم لعارض كالعلمية[[٢]] مثلا، لم يقو قوة اللزوم[[٣]] الوضعي.",
     "en": "so were inseparability to arise through some accidental factor (ʿāriḍ), such as being a proper name (ʿalamiyya) for instance, it would not attain the strength of inseparability grounded in the original coinage (al-luzūm al-waḍʿī)."},

    # ---------------- Section heading ----------------
    {"type": "section", "ar": "[العدل]",
     "en": "Deviation (al-ʿAdl)"},

    {"type": "matn",
     "ar": "(فالعدل[[٤]]) مصدر مبني للمفعول[[٥]]، أي: كون الاسم معدولا (خروجه[[٦]]) أي: خروج الاسم، أي: كونه مخرجا (عن صيغته[[٧]] الأصلية)",
     "en": "(So deviation, al-ʿadl) is a verbal noun of the passive voice, that is: the noun’s being deviated (maʿdūl); (is its departure, khurūjuhu) — that is, the departure of the noun, meaning its being made to depart (from its original form, ʿan ṣīghatihi al-aṣliyya)"},

    {"type": "matn",
     "ar": "أي: عن صورته التي يقتضي الأصل والقاعدة أن يكون ذلك الاسم عليها[[٨]].",
     "en": "that is: from its form which the fundamental principle and the rule require that noun to be upon."},

    {"type": "matn",
     "ar": "ولا يخفى عليك أن صيغة المصدر ليست صيغة المشتقات، فبإضافة الصيغة إلى ضمير الاسم خرجت المشتقات كلها.",
     "en": "It is not hidden from you that the form of the verbal noun (maṣdar) is not the form of the derivatives (mushtaqqāt); so by annexing “the form” to the pronoun [referring to] “the noun,” all the derivatives are excluded."},

    {"type": "matn",
     "ar": "وإن المتبادر من خروجه عن صيغته الأصلية أن تكون المادة باقية، والتغيير إنما...",
     "en": "and that what comes readily to mind from its departure from its original form is that the material root (mādda) remains, and the alteration is only..."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: لبنائها، وإن اتفق في بعض الأسماء لزومها كحجارة وتجارة.",
     "en": "That is: on account of its being built-in (bināʾ), even though in some nouns its inseparability happens to coincide, as in “ḥijāra” and “tijāra.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بيان للعارض، أي: لأن الأعلام لا تتغير كما أن ضروب الأمثال كذلك.",
     "en": "An elucidation of the accidental factor (ʿāriḍ); that is: because proper names do not change, just as the varieties of proverbs (amthāl) likewise [do not change]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "من باب علم. وقوة منصوب بنزع الخافض، أي: مثل قوة اللزوم الوضعي الكائن في مثل حبلى وحمراء.",
     "en": "[The verb “yaqwā”] is of the pattern of “ʿalima.” And “qūwa” is accusative through the removal of the governing preposition (nazʿ al-khāfiḍ) — that is: “like the strength of the coinage-based inseparability present in the likes of ḥublā and ḥamrāʾ.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الفاء لتفسير العدل وأخواته، أي: بيان نفس مفهوم السبب، أو شرط تأثيره وعليته، وهو في اللغة: الصرف، يقال: اسم معدول، أي: مصروف عن بنيته.",
     "en": "The fāʾ is for explicating “al-ʿadl” and its cognates — that is, an elucidation of the very concept of the cause (sabab), or of the condition of its effect and its causality; and it (al-ʿadl), in language, means “diversion” (al-ṣarf). One says “ismun maʿdūl” (a deviated noun), that is, one diverted from its [original] structure (bunya)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فيصح تفسيره بالخروج؛ لأن مفهومه أعم من أن يكون مستندا إلى الإخراج أو لا، وإن كان المتبادر الخروج بنفسه.",
     "en": "So its being explained by “departure” (khurūj) is sound, because its concept is more general than being grounded in [active] causing-to-depart (ikhrāj) or not, even though what first comes to mind is departure in itself."},
    {"type": "pair",
     "ar": "وإنما لم يفسر المصنف مصدر المعلوم؛ لأنه لا يدل على ما هو مسبب للمنع إلا ضمنا؛ لأن السبب ما قام بالاسم؛ إذ به يتحقق الفرعية؛ وهو ههنا المعدولية لا ما قام بالمتكلم.",
     "en": "The author did not explain it as the verbal noun of the active voice (maṣdar al-maʿlūm) only because that would indicate what is the cause of the prevention [of full inflection] merely implicitly; for the cause is that which subsists in the noun — since through it derivativeness (farʿiyya) is realized — and that here is the state of being deviated (al-maʿdūliyya), not what subsists in the speaker."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: خروج مادته؛ إذ لا يتصور خروج الكل عن جزئه.",
     "en": "That is: the departure of its material root (mādda); since the departure of the whole from its own part is inconceivable."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "كأنه أراد بها ما يشمل صورته الحكمية أيضا، فإن خروج سحر معينا من السحر ليس خروجا عن صورته الحقيقية؛ إذ لا دخل للام فيها،",
     "en": "It is as though he intended by it [the “form”] that which includes its juridical form (al-ṣūra al-ḥukmiyya) as well, for the departure of “saḥar” — used as a determinate — from “al-saḥar” is not a departure from its real form, since the lām has no bearing upon it;"},
    {"type": "pair",
     "ar": "نعم لها دخل في صورته الحكمية؛ لأن اللام بمنزلة جزء الكلمة، ولذا لا يجوز الفصل بينها وبين مدخولها،",
     "en": "yes, it [the lām] does have a bearing on its juridical form, because the lām is tantamount to a part of the word, and therefore it is not permitted to separate between it and that which it governs;"},
    {"type": "pair",
     "ar": "ومع هذا يبقى فيه الإشكال؛ لأنها غير متناولة للصورة الحاصلة بـ«من» أو الإضافة.",
     "en": "and despite this, the difficulty remains in it, because it [the form] does not encompass the form produced by “min” or by annexation (iḍāfa)."},
    {"type": "pair",
     "ar": "ولهذا يغير التفسير بأنه خروج عما هو حقه من الصيغة، أو استلزام كلمة أخرى معه.",
     "en": "For this reason he alters the explanation [to say] that it is a departure from what is its due of form (ṣīgha), or the necessitation of another word along with it."},
    {"type": "pair",
     "ar": "وفيه أنه يلزم أن يكون يوم الجمعة معدولا عن صمت في يوم الجمعة مع أنه ليس معدولا عنه.",
     "en": "But against this stands [the objection] that it would then follow that “yawm al-jumuʿa” is a deviation from “ṣamt” in “yawm al-jumuʿa,” even though it is not something deviated from."},
    {"type": "pair",
     "ar": "ولا يرد على تفسير المصنف؛ إذ ليس لـ«في» مدخل في صورته الحكمية لجواز الفصل بينها وبين مدخولها بالحرف الزائد.",
     "en": "This does not tell against the author’s explanation, since “fī” has no bearing on its juridical form, given the permissibility of separating between it and what it governs by an additional particle (al-ḥarf al-zāʾid)."},
    {"type": "pair",
     "ar": "ويمكن أن يقال: إن ذلك الخروج غير تام؛ لأن المقدر في حكم الملفوظ.",
     "en": "And it may be said: that departure is not complete, because what is elided (al-muqaddar) has the status of what is pronounced (al-malfūẓ)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "خروج الاسم عن صيغته الأصلية بهذا المعنى في «عمر» غير ظاهر؛ لأنه ليس هناك أصل وقاعدة يقتضي أن يكون «عمر» على صيغة «عامر» إلا أن يقال:",
     "en": "The departure of the noun from its original form in this sense, in [the case of] “ʿUmar,” is not evident, because there is no fundamental principle and rule requiring that “ʿUmar” be upon the form “ʿĀmir” — unless it be said:"},
    {"type": "pair",
     "ar": "لما اقتضى ضرورة منع الصرف إلى أن يحكم بأنه معدول، حكم بأنه يسمى باسم الفاعل من العمارة، فـ«عمر» اسم الفاعل من العمارة، خرج عن صيغته التي هي على مقتضى القاعدة، وهي «عامر» إلى «عمر».",
     "en": "since the necessity of denying full inflection (manʿ al-ṣarf) required judging it to be deviated (maʿdūl), it was judged that it is named with the active participle from “al-ʿimāra” (habitation), so that “ʿUmar” is the active participle from “al-ʿimāra,” having departed from its form which accords with the requirement of the rule — namely “ʿĀmir” — to “ʿUmar.”"},
]
