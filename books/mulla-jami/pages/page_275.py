# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 275 (printed ٢٧٤)."""

PAGE_NUMBER = 275
PRINTED_PAGE = "٢٧٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لكن زيادة «من»» from the foot of PDF p. 274.
    {"type": "matn",
     "ar": "فيها[[١]] نحو: «لله دره من فارس»، وقولهم: «عز من قائل» يؤيد التمييز[[٢]]؛",
     "en": "…in it, as in “To Allah [belongs] his milk, what a horseman (min fārisin)!”, and their saying “Mighty is He as a speaker (min qāʾilin),” supports the specification;"},
    {"type": "matn",
     "ar": "لأن «من» تزاد في التمييز[[٣]] لا في الحال،",
     "en": "because “min” is added in the specification, not in the ḥāl;"},
    {"type": "matn",
     "ar": "وأيضا المقصود مدحه بالفروسية لا حال الفروسية؛ إذ قد يمدح حال الفروسية بغيرها من الصفات.",
     "en": "and further, what is intended is to praise him for horsemanship, not in the state of horsemanship; for one may be praised in the state of horsemanship for other qualities."},
    {"type": "matn",
     "ar": "(ولا يتقدم التمييز على عامله) إذا كان اسما تاما بالاتفاق[[٤]]، فلا يقال: «عندي درهما عشرون» ولا «زيتا رطل»؛",
     "en": "(The specification does not precede its governor) when [the governor] is a complete noun, by agreement; so one does not say “I have, as dirhams, twenty,” nor “as oil, a raṭl”;"},
    {"type": "matn",
     "ar": "لأن عامله حينئذ اسم جامد ضعيف العمل مشابه للفعل مشابهة ضعيفة كما ذكرناه، فلا يقوى أن يعمل فيما قبله.",
     "en": "because its governor in that case is a primitive (jāmid) noun, weak in governing, resembling the verb only weakly, as we have mentioned; so it is not strong enough to govern what precedes it."},
    {"type": "matn",
     "ar": "(والأصح) أي: أصح المذاهب (ألا يتقدم) التمييز (على) ما هو عامل فيه من (الفعل) الصريح أو الغير الصريح،",
     "en": "(The soundest)—that is, the soundest of the doctrines—(is that) the specification (does not precede) what governs it of (the verb), explicit or non-explicit,"},
    # REVIEW: print reads «طاب زيدا أبا» (accusative «زيدا»; sense requires «زيد»); transcribed as printed.
    {"type": "matn",
     "ar": "لكونه من حيث المعنى فاعلا[[٥]] للفعل نفسه نحو: «طاب زيدا أبا» أي: طاب أبوه،",
     "en": "because in meaning it is the agent of the verb itself, as in “Zayd is good in respect of father,” that is, his father is good;"},
    {"type": "matn",
     "ar": "أو فاعلا له إذا جعلته لازما[[٦]] نحو: ﴿وفجرنا الأرض عيونا﴾[[٧]] أي: انفجرت عيونها،",
     "en": "or the agent of it when you take it as intransitive, as in “And We caused the earth to burst forth with springs,” that is, its springs burst forth;"},
    {"type": "matn",
     "ar": "وإذا جعلته متعديا نحو: «امتلأ الإناء ماء» أي: «ملأه الماء»، والفاعل لا يتقدم على الفعل، فكذا ما هو بمعنى الفاعل.",
     "en": "and when you take it as transitive, as in “The vessel became full of water,” that is, “the water filled it.” The agent does not precede the verb, and likewise what has the sense of the agent."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "زيادة «من» في التمييز عن ذات مذكورة يجوز مطلقا. ويجوز في التمييز عن الذات المقدرة إذا كان لما انتصب عنه.",
     "en": "Adding “min” in the specification of a mentioned entity is permissible without restriction; and it is permissible in the specification of the implied entity when it belongs to that from which it takes the accusative."},
    {"type": "pair",
     "ar": "وقيل: مطلقا كذا ذكره الشيخ الرضي، وأنكر المقتبس صحة عشرون من درهم،",
     "en": "It has been said: without restriction. So Shaykh al-Raḍī mentioned. The author of al-Muqtabas rejected the correctness of “twenty of dirham,”"},
    {"type": "pair",
     "ar": "وكان المصنف معه حيث صرح بتجويز دخول «من» على مميز «كم»،",
     "en": "and the author [Ibn al-Ḥājib] was with him, in that he explicitly allowed “min” to enter upon the specified term of “kam”;"},
    {"type": "pair",
     "ar": "فلو كان تجويز دخول «من» على التمييز من الذات المذكورة عاما لم يخصهما بهذا الحكم، فتأمل.",
     "en": "for had allowing “min” to enter upon the specification of a mentioned entity been general, he would not have singled out those two with this ruling. So reflect."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قلت: بل زيادة «من» يؤيد احتمال الحال؛ إذ زيادة «من» ليكون تنصيصا على أن المراد التمييز لا الحال.",
     "en": "I say: rather, adding “min” supports the possibility of the ḥāl; for “min” is added to make explicit that what is meant is the specification, not the ḥāl."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "في قسمه الأول مطلقا. وفي قسمه الثاني إذا كان لما انتصب عنه.",
     "en": "In its first division without restriction; and in its second division when it belongs to that from which it takes the accusative."},
    {"type": "pair",
     "ar": "وقيل: مطلقا هكذا قال الشيخ الرضي.",
     "en": "It has been said: without restriction. So said Shaykh al-Raḍī."},
    {"type": "pair",
     "ar": "وقال في المقتبس: يقال: لله دره من فارس، ولا يقال: عندي عشرون من درهم.",
     "en": "He said in al-Muqtabas: one says “To Allah [belongs] his milk, what a horseman (min fārisin)!”, but one does not say “I have twenty of dirham.”"},
    {"type": "pair",
     "ar": "والفرق أن الأول كما يحتمل التمييز يحتمل الحال، فـ«من» يخلصه للتمييز.",
     "en": "The difference is that the first, just as it admits the specification, admits the ḥāl, so “min” makes it purely a specification."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يشكل بما إذا كان تمييزا عن نسبة اسم الفاعل أو المفعول، فإنه يتقدم التمييز على عامله عند الجمهور مع أن عامله اسم تام هو اسم الفاعل أو المفعول،",
     "en": "This is problematic where it is a specification of the relation of an active or passive participle; for there the specification precedes its governor according to the majority, although its governor is a complete noun, namely the active or passive participle."},
    {"type": "pair",
     "ar": "فالأولى أن يقول: لا يتقدم التمييز على عامله إذا كان عن ذات مذكورة بالاتفاق.",
     "en": "So it would be better to say: the specification does not precede its governor when it is [a specification] of a mentioned entity, by agreement."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ولفوات الغرض من التمييز، وهو البيان بعد الإجمال ليكون أوقع،",
     "en": "And because the purpose of the specification would be lost, namely clarification after summary statement, so that it has greater effect;"},
    {"type": "pair",
     "ar": "لكن البيان بـ«من» البيانية لا يمنع من التقديم كما في قوله تعالى: ﴿فغشيهم من اليم ما غشيهم﴾ (سورة طه:٧٨).",
     "en": "but clarification by the explicative “min” does not prevent fronting, as in His words, the Exalted: “And there covered them of the sea that which covered them” (Qurʾān, Sūrat Ṭā Hā 20:78)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يعني: أن التمييز فاعل لهذا الفعل، أو ما ينوب منابه في تركيب يؤدي مضمون هذه الجملة، فبهذا الاعتبار جعل كالفاعل له،",
     "en": "He means that the specification is the agent of this verb, or of what stands in its place in a construction that conveys the content of this sentence; in this respect it was treated as its agent."},
    {"type": "pair",
     "ar": "وليس المعنى أن ﴿وفجرنا الأرض عيونا﴾ (سورة القمر:١٢)، فجر فيه منزل منزلة اللازم لتضمنه معنى الانفجار، وعيونا تمييز عن نسبة الانفجار،",
     "en": "The meaning is not that in “And We caused the earth to burst forth with springs” (Qurʾān, Sūrat al-Qamar 54:12) fajjara is treated as intransitive because it implies the meaning of bursting forth, with “springs” a specification of the relation of bursting forth;"},
    {"type": "pair",
     "ar": "لعدم احتمال سوق العبارة إياه، وإلا لقال: أو فاعلا لما يتضمنه.",
     "en": "for the course of the wording does not admit this; otherwise he would have said: “or the agent of what it implies.”"},
    {"type": "pair",
     "ar": "وكذا الحال في امتلأ الإناء ماء، فمن بنى الكلام على تضمين المثالين، فضمان تصحيح كلامه عليه.",
     "en": "The same holds for “The vessel became full of water.” Whoever builds the discussion on implication (taḍmīn) in the two examples bears the burden of making his words correct."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سورة القمر: ١٢.",
     "en": "Qurʾān, Sūrat al-Qamar 54:12."},
]
