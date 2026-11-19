# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 409 (printed ٤٠٨)."""

PAGE_NUMBER = 409
PRINTED_PAGE = "٤٠٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «...والأشهر بقاؤه على بنائه لشذوذ الإضافة إلى المفرد.» at the foot of PDF p. 408 (new sentence).
    {"type": "matn",
     "ar": "(ومنها) أي: من الظروف المبنية («إذا»[[١]]) زمانية كانت أو مكانية، وإنما بنيت لما ذكرنا في «حيث»[[٢]]",
     "en": "(And among them), that is, among the indeclinable adverbs, is (“idhā”), whether temporal or spatial; it is indeclinable only for the reason we gave for “ḥaythu”."},
    {"type": "matn",
     "ar": "(وهي) إذا كانت[[٣]] زمانية (للمستقبل) أي: للزمان المستقبل، وإن كانت داخلا على الماضي،",
     "en": "(And it), when it is temporal, (is for the future), that is, for future time, even when it is attached to the past [tense verb]."},
    {"type": "matn",
     "ar": "وذلك لأن الأصل في استعمالها أن يكون لزمان من أزمنة المستقبل مختص من بينها بوقوع حدث فيه مقطوع بوقوعه في اعتقاد المتكلم،",
     "en": "That is because the basic rule in its use is that it be for a time among the times of the future that is singled out from among them by the occurrence in it of an event whose occurrence is certain in the speaker’s belief."},
    {"type": "matn",
     "ar": "والدليل عليه استعمالها في الأغلب الأكثر في هذا المعنى، نحو: «إذا طلعت الشمس»، وقوله تعالى: ﴿إذا الشمس كورت﴾[[٤]]،",
     "en": "The proof of this is its use, in the great majority of cases, in this sense, as in “idhā ṭalaʿati al-shamsu” (when the sun rises), and His words, the Exalted: “When the sun is wrapped up”."},
    {"type": "matn",
     "ar": "ولهذا كثر في الكتاب العزيز استعماله، لقطع علام الغيوب بالأمور المتوقعة،",
     "en": "For this reason its use is frequent in the Mighty Book, since the Knower of the unseen is certain of the things expected."},
    {"type": "matn",
     "ar": "وقد استعمل في الماضي كما في قوله تعالى: ﴿حتى إذا بلغ بين السدين﴾[[٥]]، و﴿حتى إذا ساوى بين الصدفين﴾[[٦]]، و﴿حتى إذا جعله نارا﴾[[٧]].",
     "en": "It has been used for the past, as in His words, the Exalted: “Until, when he reached [the place] between the two barriers”, and “until, when he had levelled [them] between the two mountain sides”, and “until, when he had made it [like] fire”."},
    {"type": "matn",
     "ar": "(وفيها) أي: في «إذا» (معنى الشرط) وهو ترتب مضمون جملة على أخرى[[٨]]،",
     "en": "(And in it), that is, in “idhā”, (is the meaning of condition), which is the content of one sentence being consequent upon another,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: the note opens «الحكم ببناء؛ إذ استدلال...» as printed (confirmed at 700 dpi); the sense is elliptical.
    {"type": "pair",
     "ar": "الحكم ببناء؛ إذ استدلال من غير شاهد الاستعمال يقاس في الحكم ببنائها على ما يشاهد بناؤها مما يشاركها في موجب البناء بخلاف «متى وأين أنى وكيف»،",
     "en": "The judgement of indeclinability [rests on inference], since it is an inference without the witness of usage: in judging it indeclinable it is compared with words whose indeclinability is witnessed and which share with it the cause of indeclinability; unlike “matā, ayna, annā and kayfa”,"},
    {"type": "pair",
     "ar": "فإن عدم التنوين فيها شاهد البناء",
     "en": "for the absence of nunation in them is a witness of indeclinability."},
    {"type": "pair",
     "ar": "والعامل في الظروف المتضمنة معنى الشرط سوى «إذا» هو الشرط عند الأكثرين، وفي «إذا» الجزاء عند الأكثرين.",
     "en": "The governor in the adverbs containing the meaning of condition, other than “idhā”, is the condition clause according to most; and in “idhā” it is the apodosis (jazāʾ) according to most."},
    {"type": "pair",
     "ar": "والرضي رجح قولهم فيما سوى «إذا»، واختار التفصيل في «إذا» بأنه إذا قصد به معنى الشرط، فالقول قولهم وإن جرد لمعنى الظرفية، فالعامل ما هو في موقع الجزاء.",
     "en": "Al-Raḍī preferred their view for what is other than “idhā”, and chose a distinction for “idhā”: when the meaning of condition is intended by it, the view is theirs; and when it is stripped down to the meaning of adverbiality, the governor is what stands in the position of the apodosis."},
    # REVIEW: the clauses read awkwardly as printed («فالقول قولهم وإن جرد ... فالعامل ما هو في موقع الجزاء»); transcribed as printed.

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "في الرضي: وأما إذا ففيها خلاف هل هي مضافة إلى الشرط أو لا، انتهى.",
     "en": "In al-Raḍī: “As for ‘idhā’, there is disagreement about it, whether it is annexed to the condition clause or not.” End of quotation."},
    {"type": "pair",
     "ar": "فالدليل المذكور في «حيث» إنما يجري على مذهب من قال بإضافتها إلى الشرط، وأنها ظرف للجزاء كما هو المشهور.",
     "en": "So the proof given for “ḥaythu” applies only on the doctrine of one who holds that it is annexed to the condition clause and that it is an adverb for the apodosis, as is the well-known view."},
    {"type": "pair",
     "ar": "وأما على القول بأنها مقطوعة عنها، والعامل فيها الشرط فلا،",
     "en": "But on the view that it is cut off from it, and that its governor is the condition clause, it does not."},
    {"type": "pair",
     "ar": "والأولى ما قاله الشيخ ابن الحاجب: إنما بني «حيث وإذ وإذا»؛ لأنها موضوعة لمكان حدث تتضمنه الجملة أو زمانه، فشابهت الموصولات في احتياجها إلى الجملة.",
     "en": "Better is what Shaykh Ibn al-Ḥājib said: “ḥaythu”, “idh” and “idhā” are indeclinable only because they are coined for the place of an event contained in the sentence, or its time; so they resemble the relative nouns in needing a sentence."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إشارة إلى أن قوله: للمستقبل خبر مبتدأ محذوف مع تقدير العاطف بقرينة كونه حكما كالأحكام المذكورة بعده بالواو،",
     "en": "An indication that his words “for the future” are the predicate of an omitted subject, with a conjunction supposed, on the evidence of its being a ruling like the rulings mentioned after it with “wa”."},
    {"type": "pair",
     "ar": "ولا يصح جعله حالا ولا صفة؛ لأن «إذا» من الظروف المبنية سواء كان للمستقبل أو للماضي أو للحال أو للاستمرار، فإذا لا يكون شيئا منهما.",
     "en": "It cannot be made a ḥāl nor a qualifier, because “idhā” is among the indeclinable adverbs whether it is for the future, the past, the present or continuity; so it is neither of the two."},
    {"type": "pair",
     "ar": "وقيل: الجملة معترضة، فلا حاجة إلى تقدير العطف، لكن كونه حكما كسائر الأحكام يزيف الاعتراض.",
     "en": "It has been said that the sentence is parenthetical, so there is no need to suppose a conjunction; but its being a ruling like the other rulings invalidates [the claim of] parenthesis."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة التكوير: ١.",
     "en": "Qurʾān, Sūrat al-Takwīr 81:1."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة الكهف: ٩٣.",
     "en": "Qurʾān, Sūrat al-Kahf 18:93."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة الكهف: ٩٦.",
     "en": "Qurʾān, Sūrat al-Kahf 18:96."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سورة الكهف: ٩٦.",
     "en": "Qurʾān, Sūrat al-Kahf 18:96."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لكن يفرق بين تضمين «إذا» وسائر أسماء الشرط من «متى» ونظائرها، فإن «إذا» غير راسخة في معنى الشرط، ولا عراقة لها فيه.",
     "en": "But a distinction is made between the inclusion [of the conditional meaning] in “idhā” and in the other conditional nouns such as “matā” and its like: “idhā” is not firmly rooted in the meaning of condition and has no deep-seated place in it."},
    # Footnote ٨ runs on to PDF p. 410.
    {"type": "pair",
     "ar": "ولذا جاء جزاؤها الاسمية بغير فاء وإذا كقوله تعالى: ﴿وإذا ما غضبوا هم",
     "en": "For this reason its apodosis, when nominal, comes without “fa” or [the surprise] “idhā”, as in His words, the Exalted: “And when they are angry, they…"},
]
