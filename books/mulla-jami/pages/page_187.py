# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 187 (printed ١٨٦)."""

PAGE_NUMBER = 187
PRINTED_PAGE = "١٨٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "١-(جوازا كقولك: لمن قدم) من سفره: (خير مقدم[[١]]) أي: قدمت قدوما خير مقدم،",
     "en": "…1. (permissibly—jawāzan, as in your saying to one who has arrived) from his journey: (“the best of arrivals”—khayra maqdamin), that is: you have arrived with an arrival that is the best of arrivals."},
    {"type": "matn",
     "ar": "فـ«خير» اسم تفضيل، ومصدريته باعتبار الموصوف أو المضاف إليه؛ لأن اسم التفضيل له حكم ما أضيف إليه[[٢]].",
     "en": "So “khayra” is an elative noun (ism tafḍīl), and its being a maṣdar is by virtue of the qualified noun or the noun to which it is annexed; because the elative takes the status of that to which it is annexed."},
    {"type": "matn",
     "ar": "٢-(ووجوبا[[٣]]) أي: حذفا واجبا[[٤]] (سماعا) أي: سماعيا[[٥]] موقوفا على السماع لا قاعدة له يعرف بها[[٦]].",
     "en": "2. (And obligatorily—wa-wujūban), that is: an obligatory elision, (by audition—samāʿan), that is: auditory (samāʿī), dependent on what is heard [from the Arabs], with no rule by which it is known."},
    {"type": "matn",
     "ar": "(نحو: سقيا) أي: «سقاك الله سقيا»[[٧]].",
     "en": "(As in: “a watering”—saqyan), that is: “May Allah water you with a watering.”"},
    {"type": "matn",
     "ar": "(ورعيا) أي: «رعاك الله رعيا»[[٨]].",
     "en": "(And “a pasturing”—wa-raʿyan), that is: “May Allah pasture you with a pasturing.”"},
    {"type": "matn",
     "ar": "(وخيبة) أي: «خاب خيبة» من خاب الرجل خيبة إذا لم ينل ما طلبه.",
     "en": "(And “a disappointment”—wa-khaybatan), that is: “May he be disappointed with a disappointment,” from khāba al-rajulu khaybatan, said when a man does not attain what he sought."},
    {"type": "matn",
     "ar": "(وجدعا) أي: «جدع جدعا» والجدع: قطع الأنف والأذن[[٩]] والشفة واليد.",
     "en": "(And “a mutilation”—wa-jadʿan), that is: “May he be mutilated with a mutilation”; jadʿ is the cutting off of the nose and the ear and the lip and the hand."},
    {"type": "matn",
     "ar": "(وحمدا) أي: «حمدت حمدا».",
     "en": "(And “praise”—wa-ḥamdan), that is: “I have praised with praise.”"},
    {"type": "matn",
     "ar": "(وشكرا) أي: «شكرت شكرا».",
     "en": "(And “thanks”—wa-shukran), that is: “I have thanked with thanks.”"},
    {"type": "matn",
     "ar": "(وعجبا) أي: «عجبت عجبا»،",
     "en": "(And “wonder”—wa-ʿajaban), that is: “I have wondered with wonder.”"},
    {"type": "matn",
     "ar": "فإنه لم يوجد في كلامهم استعمال الأفعال العاملة في هذه المصادر، وهذا معنى وجوب الحذف سماعا[[١٠]].",
     "en": "For the use of the verbs governing these maṣdars is not found in their speech; and this is the meaning of obligatory elision by audition."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وحينئذ يكون خبرا أو دعاء.",
     "en": "In that case it is either a statement or a supplication."},
    {"type": "pair",
     "ar": "وكذا إذا قيل لمن يمضي إلى السفر، وحينئذ يكون دعاء.",
     "en": "Likewise when it is said to one setting out on a journey; in that case it is a supplication."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لما ذكرنا من أنه بعض ما أضيف إليه.",
     "en": "On account of what we mentioned: that it is a part of that to which it is annexed."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "عطف على قوله: «جوازا» بمعنى: وقد يحذف الفعل الناصب للمفعول المطلق لقيام قرينة وجوبا.",
     "en": "It is coordinated with his word “jawāzan,” meaning: and the verb that puts the absolute object in the accusative may be elided, on account of the presence of a contextual indication, obligatorily."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أشار إلى أن وجوبا منصوب على المصدرية باعتبار أنه بمعنى اسم الفاعل، وصفة للمصدر المحذوف.",
     "en": "He indicated that “wujūban” is accusative as a maṣdar, in that it has the sense of an active participle (ism al-fāʿil) and is an adjective of the elided maṣdar."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فيكون صفة لـ«وجوبا» أو حالا عنه.",
     "en": "So it is an adjective of “wujūban” or a circumstantial qualifier (ḥāl) of it."},
    {"type": "pair",
     "ar": "ويجوز أن يكون مفعولا مطلقا بتقدير: سمع سماعا.",
     "en": "It may also be an absolute object, on the supposition: “it was heard with a hearing.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يعني: أن نسبة هذا الحذف إلى السماع باعتبار أن يسمع من العرب بحيث لم يثبت الفعل أصلا بسبب وجوب الحذف من غير قاعدة يعرف بها وجوب الحذف.",
     "en": "He means: the ascription of this elision to audition is in respect of its being heard from the Arabs in such a way that the verb is not attested at all, owing to the obligatoriness of the elision, without a rule by which the obligatoriness of the elision is known."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "هذا دعاء باعتبار ذات المخاطب أو باعتبار فروعه.",
     "en": "This is a supplication with respect to the person addressed himself, or with respect to his branches (furūʿ)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "هذا أيضا دعاء له: إما باعتبار ذات المخاطب بأن رزقه الله تعالى من حيث لا يحتسب في الخصب والرخاء،",
     "en": "This too is a supplication for him: either with respect to the person addressed himself, that Allah the Exalted provide for him from where he does not reckon, in fertility and ease,"},
    {"type": "pair",
     "ar": "أو باعتبار مواشيه بأن جعل الله مرعاها ذي نباتات طرية كثيرة.",
     "en": "or with respect to his livestock, that Allah make their pasture abound in fresh plants."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "في الرضي: كلمة «أو» بدل كلمة \"و\"، وهو الموافق للغة.",
     "en": "In al-Raḍī: the word “aw” (or) in place of the word “wa” (and); and that is what agrees with the lexicon."},
    {"type": "pair",
     "ar": "وهو دعاء عليه بالذل وقبح الحال.",
     "en": "It is an imprecation against him of abasement and an ugly state."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "لا يخفى أنه لو كان معنى وجوب الحذف سماعا هذا لكان القياسي أيضا واجب الحذف سماعا؛ لأنه لم يوجد في كلام العرب استعمال الأفعال العاملة فيه،",
     "en": "It is not hidden that, were this the meaning of obligatory elision by audition, the analogical (qiyāsī) [case] would also be obligatorily elided by audition; because the use of the verbs governing it is likewise not found in the speech of the Arabs."},
    {"type": "pair",
     "ar": "بل معنى وجوب الحذف سماعا أنه لم يوجد استعمال الأفعال العاملة فيه، ولا قاعدة له يعرف بها.",
     "en": "Rather, the meaning of obligatory elision by audition is that the use of the verbs governing it is not found, and there is no rule for it by which it is known."},
]
