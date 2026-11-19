# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 276 (printed ٢٧٥)."""

PAGE_NUMBER = 276
PRINTED_PAGE = "٢٧٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "وههنا بحث[[١]]، وهو أن الماء في قولهم: «امتلأ الإناء ماء» من حيث المعنى فاعل للفعل المذكور من غير حاجة إلى جعله متعديا؛",
     "en": "There is a point for discussion here: “water” in their saying “The vessel became full of water” is, in meaning, the agent of the verb mentioned, with no need to take it as transitive;"},
    {"type": "matn",
     "ar": "لأن المتكلم لما قصد[[٢]] إسناد الامتلاء إلى بعض متعلقات الإناء، ولو على سبيل التجوز وقدره، وقع الإبهام فيه لا جرم فميزه بقوله: «ماء»،",
     "en": "for since the speaker intended to attribute fullness to something connected with the vessel—even by way of figurative usage—and implied it, indefiniteness arose in it, and so he necessarily specified it by saying “water”;"},
    {"type": "matn",
     "ar": "فهو في معنى: «امتلأ ماء الإناء»، فالماء فاعل معنى،",
     "en": "so it has the sense of “The water of the vessel became full,” and “water” is the agent in meaning."},
    {"type": "matn",
     "ar": "وذلك بعينه مثل قولك: «ربح زيد تجارة»[[٣]]، فإن التجارة تمييز يرفع الإبهام عن شيء منسوب إلى زيد، وهو التجارة،",
     "en": "This is exactly like your saying “Zayd profited in trade”: “trade” is a specification removing the indefiniteness from something attributed to Zayd, namely the trade;"},
    {"type": "matn",
     "ar": "فالفاعل في قصدك هو التجارة لا زيد، وإن كان إسناد الربح إليه حقيقة وإليها مجازا،",
     "en": "so the agent in your intention is the trade, not Zayd, even though attributing profit to him is literal and to it figurative."},
    {"type": "matn",
     "ar": "وبهذا يندفع ما يورد على قاعدتهم المشهورة، وهي أن التمييز[[٤]] عن النسبة إما فاعل في المعنى أو مفعول",
     "en": "By this is repelled the objection raised against their well-known rule, namely that the specification of a relation is either an agent in meaning or an object—"},
    {"type": "matn",
     "ar": "من أن التمييز في هذا المثال وأمثاله لا فاعل ولا مفعول، فلا تطرد تلك القاعدة.",
     "en": "[the objection] that the specification in this example and its like is neither agent nor object, so that the rule does not hold generally."},
    {"type": "matn",
     "ar": "(خلافا للمازني[[٥]] والمبرد) فإنهما يجوزان تقدم التمييز على الفعل الصريح وعلى اسمي الفاعل والمفعول[[٦]] نظرا إلى قوة العامل[[٧]]،",
     "en": "(Contrary to al-Māzinī and al-Mubarrad), for they both allow the specification to precede the explicit verb and the active and passive participles, in view of the strength of the governor,"},
    {"type": "matn",
     "ar": "بخلاف الصفة المشبهة واسم التفضيل والمصدر وما فيه معنى الفعل، لضعفها في العمل",
     "en": "unlike the qualificative adjective, the elative, the verbal noun and what carries the meaning of the verb, because of their weakness in governing."},
    {"type": "matn",
     "ar": "ومتمسكهما في هذا التجويز قول الشاعر[[٨]]:",
     "en": "Their support for this allowance is the poet's saying:"},
    {"type": "verse",
     "ar": "أتهجر سلمى بالفراق حبيبها          وما كاد نفسا[[٩]] بالفراق[[١٠]] تطيب",
     "en": "Will Salmā forsake her beloved by parting, when [her] soul was scarcely content with parting?"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ليس البحث واردا؛ لأن سر وجوب تأخير التمييز عن العامل كونه فاعلا: إما حقيقيا لو رد الفعل المذكور إلى المتعدي، وإما مجازيا إن لم يرد",
     "en": "The point for discussion does not apply; because the reason the specification must come after the governor is its being an agent: either a literal one, if the verb mentioned is turned into a transitive, or a figurative one, if it is not;"},
    {"type": "pair",
     "ar": "إلا أنهم تعرضوا لكونه فاعلا حقيقيا بالرد إظهارا لما خفي من الوجه.",
     "en": "except that they addressed its being a literal agent by [this] turning, to bring out the aspect that was hidden."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بقرينة دالة على أن الظاهر غير مراد.",
     "en": "With a contextual indication (qarīna) showing that the apparent sense is not meant."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "مغير ربح تجارة زيد، كقوله تعالى: ﴿فما ربحت تجارتهم﴾ (سورة البقرة:١٦).",
     "en": "Altered from “Zayd's trade profited,” as in His words, the Exalted: “So their trade did not profit” (Qurʾān, Sūrat al-Baqara 2:16)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قاعدتهم المشهورة أن التمييز عن النسبة إما فاعل في المعنى. ولهذا احتاجوا إلى تأويل: ﴿وفجرنا الأرض عيونا﴾ (سورة القمر:١٢).",
     "en": "Their well-known rule is that the specification of a relation is either an agent in meaning [or an object]. For this reason they needed to interpret “And We caused the earth to burst forth with springs” (Qurʾān, Sūrat al-Qamar 54:12)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أستاذ المبرد وتلميذ الأخفش.",
     "en": "The teacher of al-Mubarrad and the student of al-Akhfash."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فكلام المصنف قاصر؛ لأنه إن أريد بالفعل مجرد الفعل يفيد أن خلاف المازني والمبرد في مجرده",
     "en": "So the author's statement falls short; because if by “the verb” the bare verb is meant, it conveys that the disagreement of al-Māzinī and al-Mubarrad concerns the bare [verb] alone;"},
    {"type": "pair",
     "ar": "وإن أريد به الفعل وشبهه كما هو المستفيض من كلامهم يفيد أن خلافهم في جميع ما يشبهه الفعل.",
     "en": "and if the verb and what resembles it is meant, as is widely current in their usage, it conveys that their disagreement concerns everything that resembles the verb."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قال سيبويه: كلام العرب استقراء لا قياس.",
     "en": "Sībawayh said: the speech of the Arabs is [known by] induction (istiqrāʾ), not analogy (qiyās)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "هو من مجيدي الشعراء.",
     "en": "He is among the accomplished poets."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "قيل: الرواية الصحيحة: وما كاد نفسي، فلا تمسك.",
     "en": "It has been said: the correct transmission is “wa-mā kāda nafsī” (my soul was scarcely), so there is no support [in it]."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "في بعض الروايات: بالعراق.",
     "en": "In some transmissions: “bi-l-ʿIrāq” (in Iraq)."},
]
