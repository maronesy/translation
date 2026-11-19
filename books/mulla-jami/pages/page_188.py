# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 188 (printed ١٨٧)."""

PAGE_NUMBER = 188
PRINTED_PAGE = "١٨٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "قيل: عليه قد قالوا: «حمدت الله حمدا[[١]]، وشكرته شكرا، وعجبت عجبا».",
     "en": "It has been objected against this: they have said, “I praised Allah with praise, and I thanked Him with thanks, and I wondered with wonder.”"},
    {"type": "matn",
     "ar": "فأجاب بعضهم[[٢]]: بأن ذلك ليس من كلام الفصحاء.",
     "en": "Some of them answered that this is not from the speech of the eloquent (al-fuṣaḥāʾ)."},
    {"type": "matn",
     "ar": "وبعضهم: بأن وجوب الحذف[[٣]] إنما هو فيما استعمل باللام، نحو: «حمدا له، وشكرا له، وعجبا له».",
     "en": "And some of them [answered] that the obligatoriness of elision applies only to what is used with the lām, as in: “Praise to Him, and thanks to Him, and wonder at him” (ḥamdan lahu, wa-shukran lahu, wa-ʿajaban lahu)."},
    {"type": "matn",
     "ar": "(و) قد يحذف الفعل الناصب للمفعول المطلق حذفا واجبا (قياسا) أي: حذفا قياسيا يعلم له ضابط كلي يحذف معه الفعل لزوما (في مواضع) متعددة:",
     "en": "(And) the verb that puts the absolute object in the accusative may be elided obligatorily (by analogy—qiyāsan), that is: an analogical elision for which a universal criterion (ḍābiṭ kullī) is known, with which the verb is necessarily elided, (in [several] places—fī mawāḍiʿa):"},
    {"type": "matn",
     "ar": "(منها[[٤]]) أي: من هذه المواضع موضع (ما وقع) أي: مفعول مطلق وقع (مثبتا[[٥]]) أي: أريد إثباته[[٦]] لا نفيه،",
     "en": "(Among them)—that is, among these places—is the place of (what occurs), that is, an absolute object that occurs (affirmed—muthbatan), that is: whose affirmation, not its negation, is intended;"},
    {"type": "matn",
     "ar": "فإنه لو أريد نفيه[[٧]] نحو: «ما زيد سيرا» لا يجب حذفه",
     "en": "for if its negation were intended, as in: “Zayd is not [going] a going” (mā Zaydun sayran), its [verb’s] elision is not obligatory,"},
    {"type": "matn",
     "ar": "(بعد نفي) داخل على اسم لا يكون المفعول المطلق خبرا عنه (أو) بعد (معنى نفي",
     "en": "(after a negation—baʿda nafyin) that enters upon a noun of which the absolute object cannot be the predicate, (or) after (the sense of a negation…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: أن هذه المصادر الثلاثة ليست مما وجب حذف عاملها سماعا، كما ذكره المصنف،",
     "en": "He means: these three maṣdars are not among those whose governor is obligatorily elided by audition, as the author stated;"},
    {"type": "pair",
     "ar": "فإنهم قد قالوا: حمدت الله حمدا إلى آخره بذكر الأفعال العاملة فيها.",
     "en": "for they have said “I praised Allah with praise,” and so on, mentioning the verbs governing them."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يخفى أن الجواب الأول بعيد، وإن كان موافقا لما ذكره المصنف.",
     "en": "It is not hidden that the first answer is far-fetched, even though it agrees with what the author stated."},
    {"type": "pair",
     "ar": "الجواب الثاني يقتضي أن يقال في المثال: حمدا له، وشكرا له، وعجبا له باللام.",
     "en": "The second answer requires that one say in the example: “ḥamdan lahu, wa-shukran lahu, wa-ʿajaban lahu,” with the lām."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: الذي أرى أن هذه المصادر وأمثالها إذا بين فاعلها أو مفعولها بالإضافة أو بحرف الجر، ولم يقصد بها بيان النوع وجب حذف نواصبها، يعني: قياسا، وإذا لم يبين لم يجب.",
     "en": "Shaykh al-Raḍī said: What I hold is that these maṣdars and their like, when their agent or their object is specified by annexation or by a preposition, and specification of kind is not intended by them, the elision of what puts them in the accusative is obligatory—meaning, by analogy; and when it is not specified, it is not obligatory."},
    {"type": "pair",
     "ar": "وذلك مثل: صبغة الله، وكتاب الله، وسبحان الله، ولبيك، وسعديك، وسحقا له، أي: بعدا له وحمدا لك.",
     "en": "That is like: “the dye of Allah” (ṣibghata Allāh), “the decree of Allah” (kitāba Allāh), “glory be to Allah” (subḥāna Allāh), “labbayka,” “saʿdayka,” and “saḥqan lahu,” that is: “away with him,” and “ḥamdan laka” (praise to You)."},
    {"type": "pair",
     "ar": "وأما انتصاب مثل قولهم: حمدت حمده، فليس على المصدر، بل هو مفعول به على جعل المصدر بمعنى المفعول.",
     "en": "As for the accusative of such as their saying “ḥamidtu ḥamdahu” (I praised [with] his praise), it is not as a maṣdar; rather it is a direct object, on taking the maṣdar in the sense of the passive participle (mafʿūl)."},
    {"type": "pair",
     "ar": "ويجوز أن تكون الإضافة في حمده لبيان النوع أي: الحمد الذي ينبغي كما في قوله تعالى: ﴿وقد مكروا مكرهم﴾ (سورة إبراهيم: ٤٦).",
     "en": "It is also possible that the annexation in “ḥamdahu” serves to specify kind, that is: the praise that is fitting, as in His saying, the Exalted: “And they had planned their plan” (Qurʾān, Sūrat Ibrāhīm 14:46)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لم يقل: هي كذا وكذا؛ لأن المواضع لا تنحصر فيما ذكر،",
     "en": "He did not say: “they are such-and-such,” because the places are not confined to what has been mentioned;"},
    {"type": "pair",
     "ar": "فإن منها المصدر الذي يقصد به التوبيخ، نحو: «أقعودا والناس قيام»، وقد تنوب الصفة مقامه نحو: «أقاعدا والناس قيام».",
     "en": "for among them is the maṣdar by which reproach (tawbīkh) is intended, as in: “Sitting, while the people are standing?” (a-quʿūdan wa-l-nāsu qiyāmun); and the adjective may stand in its place, as in: “Sitting [one], while the people are standing?” (a-qāʿidan wa-l-nāsu qiyāmun)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إنما اشترط كون المصدر مثبتا بعد نفي أو كونه مكررا؛",
     "en": "He stipulated only that the maṣdar be affirmed after a negation or that it be repeated;"},
    {"type": "pair",
     "ar": "لأن المقصود من مثل هذا الحصر أو التكرير وصف الشيء بدوام حصول الفعل منه، ولزومه له،",
     "en": "because what is intended by such restriction (ḥaṣr) or repetition is to describe the thing as continually producing the act and as being inseparable from it,"},
    {"type": "pair",
     "ar": "ووضع الفعل على التجدد، فينافيه وضعا وإن لم ينافه استعمالا، فإن المضارع قد يستعمل للدوام",
     "en": "whereas the verb is coined for renewal (tajaddud), so it conflicts with it by coinage (waḍʿan), even if it does not conflict with it in usage—for the imperfect (muḍāriʿ) is sometimes used for continuity;"},
    {"type": "pair",
     "ar": "وإن أرادوا زيادة المبالغة جعلوا المصدر نفسه خبرا، نحو: «ما زيد إلا سير» وزيد سير سير",
     "en": "and if they intended greater intensification (mubālagha), they made the maṣdar itself the predicate, as in: “Zayd is nothing but going” (mā Zaydun illā sayrun) and “Zayd is going, going” (Zaydun sayrun sayrun),"},
    {"type": "pair",
     "ar": "لينمحي عن الكلام معنى الحدث رأسا لعدم صريح الفعل وعدم المفعول الدال عليه،",
     "en": "so that the sense of the event (ḥadath) is effaced from the utterance entirely, through the absence of an explicit verb and the absence of the object indicating it;"},
    {"type": "pair",
     "ar": "ولهذا المعنى أعني: لزيادة المبالغة رفعوا بعض المصادر التي يجب حذف عاملها، نحو: «الحمد لله وسلام عليك».",
     "en": "and for this reason—I mean, for greater intensification—they put in the nominative some of the maṣdars whose governor must be elided, as in: “Praise be to Allah” (al-ḥamdu li-llāh) and “Peace be upon you” (salāmun ʿalayka)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا حاجة إلى حمل المثبت على ما أريد إثباته.",
     "en": "There is no need to interpret “affirmed” as “that whose affirmation is intended.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "وذلك لفوات الحصر الذي قصده يوجب الحذف، وكذا الحال إذا كان مثبتا، لكن لم يكن بعد نفي.",
     "en": "That is because of the loss of the restriction whose intention requires the elision; and likewise is the case when it is affirmed but does not come after a negation."},
]
