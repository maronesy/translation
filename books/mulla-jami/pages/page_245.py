# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 245 (printed ٢٤٤)."""

PAGE_NUMBER = 245
PRINTED_PAGE = "٢٤٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(وشرط نصبه) أي: شرط انتصاب المفعول له، لا شرط كون الاسم مفعولا له،",
     "en": "(The condition for its accusative), that is, the condition for the object of purpose taking the accusative, not the condition for a noun’s being an object of purpose;"},
    {"type": "matn",
     "ar": "فالسمن والإكرام في قولك: «جئتك للسمن ولإكرامك الزائر عنده» مفعول له على ما يدل عليه حده،",
     "en": "for “the butter” and “the honouring” in your saying “I came to you for the butter and for your honouring the visitor at his place” are objects of purpose, as its definition indicates."},
    {"type": "matn",
     "ar": "وهذا كما قال في المفعول فيه أن شرط نصبه تقدير «في»، وهذا أيضا خلاف اصطلاح القوم",
     "en": "This is like what he said about the mafʿūl fīhi, that the condition for its accusative is the implied presence of “fī”; and this too is contrary to the scholars’ convention."},
    {"type": "matn",
     "ar": "(تقدير اللام)؛ لأنها إذا ظهرت لزم الجر،",
     "en": "(Is the implied presence of the lām), because if it appears, the genitive becomes necessary."},
    {"type": "matn",
     "ar": "وخص اللام بالذكر[[١]]؛ لأنها الغالب في تعليلات الأفعال، فلا يقدر غيرها من «من أو الباء أو في» مع أنها من دواخل المفعول له،",
     "en": "He singled out the lām for mention because it is the prevalent one in giving the reasons for actions; so no other is implied, such as “min,” “bi-,” or “fī,” although these too are among the particles that enter upon the object of purpose,"},
    {"type": "matn",
     "ar": "كقوله تعالى: ﴿خاشعا متصدعا من خشية الله﴾[[٢]]، وقوله تعالى: ﴿فبظلم من الذين هادوا حرمنا﴾[[٣]]،",
     "en": "as in His words, the Exalted: “humbled, split asunder for fear of Allah,” and His words, the Exalted: “So for wrongdoing on the part of those who were Jews We forbade…”;"},
    {"type": "matn",
     "ar": "وقوله صلى الله تعالى عليه وسلم: «إن امرأة دخلت النار في هرة»، أي: لأجلها.",
     "en": "and his words, may Allah bless him and grant him peace: “A woman entered the Fire over (fī) a cat,” that is, for its sake."},
    {"type": "matn",
     "ar": "ولما كان تقدير اللام عبارة عن حذفها عن اللفظ، وإبقائها في النية، وكان الأصل إبقاءها في اللفظ والنية،",
     "en": "Since the implied presence of the lām means its omission from the wording and its retention in intention, and the base is to retain it in both wording and intention,"},
    {"type": "matn",
     "ar": "فلا حاجة في إبقائها في النية إلى الشرط، بل الحاجة إليه إنما يكون في حذفها من اللفظ،",
     "en": "there is no need of a condition for retaining it in intention; rather, the need for one arises only in omitting it from the wording."},
    {"type": "matn",
     "ar": "ولهذا قال: (وإنما يجوز حذفها) ولم يكتف بإرجاع ضمير الفاعل إلى تقدير اللام، فيجوز حذفها كما يجوز ذكرها",
     "en": "For this reason he said: (It may be omitted only), and did not content himself with referring the subject pronoun back to “the implied presence of the lām”; so it may be omitted just as it may be mentioned"},
    {"type": "matn",
     "ar": "(إذا كان) المفعول له (فعلا) احتراز عما إذا كان عينا[[٤]]، نحو: «جئتك للسمن»",
     "en": "(if) the object of purpose (is an action), guarding against its being a concrete thing, as in “I came to you for the butter,”"},
    {"type": "matn",
     "ar": "(لفاعل الفعل المعلل به) أي: اتحد فاعله وفاعل عامله[[٥]].",
     "en": "(of the agent of the action whose reason it gives), that is, its agent and the agent of its governor are one."},
    {"type": "matn",
     "ar": "احتراز عما إذا كان فعلا لغيره نحو: «جئتك لمجيئك إياي»",
     "en": "This guards against its being the action of another, as in “I came to you because of your coming to me,”"},
    {"type": "matn",
     "ar": "(ومقارنا له) أي: للفعل المذكور (في الوجود) بأن يتحد زمان وجودهما[[٦]] نحو: «ضربته تأديبا»؛ إذ زمان الضرب والتأديب واحد؛ إذ لا مغايرة بينهما إلا بالاعتبار،",
     "en": "(and concurrent with it), that is, with the action mentioned, (in existence), either by the times of their existence being one, as in “I struck him for discipline,” since the time of striking and of disciplining is one, there being no difference between them except in consideration;"},
    {"type": "matn",
     "ar": "أو يكون زمان وجود أحدهما[[٧]] بعضا من زمان وجود الآخر[[٨]]، نحو: «قعدت عن الحرب جبنا»، فإن زمان الفعل أعني: القعود بعض زمان المفعول له، أعني: الجبن",
     "en": "or by the time of the existence of one of them being part of the time of the existence of the other, as in “I held back from war out of cowardice,” for the time of the action, namely holding back, is part of the time of the object of purpose, namely cowardice;"},
    {"type": "matn",
     "ar": "ونحو: «شهدت الحرب",
     "en": "and as in “I witnessed the war…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "التعرض لوجه تخصيص اللام هنا دون «في» في المفعول فيه مبني على الغفلة عن أن الباء أيضا من دواخل المفعول فيه، نحو: قمت بالمسجد.",
     "en": "Addressing the reason for singling out the lām here, but not “fī” under the mafʿūl fīhi, rests on overlooking that “bi-” too is among the particles entering upon the mafʿūl fīhi, as in “I stood in (bi-) the mosque.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة الحشر: ٢١.",
     "en": "Qurʾān, Sūrat al-Ḥashr 59:21."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة النساء: ١٦٠.",
     "en": "Qurʾān, Sūrat al-Nisāʾ 4:160."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ينبغي أن يقول: احتراز عما إذا كان غير فعل ليشمل نحو: جئتك للسواد.",
     "en": "He ought to say: “guarding against its being other than an action,” so as to include such a case as “I came to you for the blackness.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أشار إلى أن المصنف لو قال هكذا لكان أولى، فإنه الواضح الأخصر.",
     "en": "He indicated that had the author put it thus, it would have been better, for it is clearer and more concise."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فالعبارة الواضحة الموجزة إنما جاز حذفها إذا اتحد فاعله وفاعل عامله وزمانهما.",
     "en": "So the clear, concise wording is: it may be omitted only when its agent and the agent of its governor, and their times, are one."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "بأن يكون آخره أول الحدث، أو بالعكس، أو بغير ذلك.",
     "en": "By its end being the beginning of the event, or the reverse, or otherwise."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    # REVIEW: «علة العقود» printed (sense requires «القعود»); transcribed as printed.
    {"type": "pair",
     "ar": "لا حاجة إلى هذا التصحيح في المثال المذكور؛ لأن علة العقود هو الجبن الموجود مع القعود لا الجبن السابق عليه،",
     "en": "There is no need for this emendation in the example mentioned, because the cause of holding back is the cowardice existing together with the holding back, not the cowardice preceding it;"},
    # REVIEW: «بعد الجبن» printed (sense suggests «يعد», “counts”); transcribed as printed.
    {"type": "pair",
     "ar": "إلا أن يقال: بعد الجبن من أوله إلى آخره جبنا واحدا لا جبنا متعددة.",
     "en": "unless it is said: cowardice is counted, from its beginning to its end, as one cowardice, not as multiple cowardices."},
]
