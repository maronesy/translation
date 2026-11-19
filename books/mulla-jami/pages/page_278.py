# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 278 (printed ٢٧٧)."""

PAGE_NUMBER = 278
PRINTED_PAGE = "٢٧٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(وهو) أي: المستثنى مطلقا حيث علم أولا بوجه يصحح تقسيمه كما عرفت، وثانيا بما يتفطن له من تعريف قسميه، أعني: المذكور بعد «إلا» وأخواتها سواء كان مخرجا أو غير مخرج،",
     "en": "(And it), that is, the excepted term (mustathnā) absolutely, since it was known first in a way that validates its division, as you have learned, and second by what is grasped from the definition of its two kinds, I mean: what is mentioned after “illā” and its sisters, whether it is extracted or not extracted;"},
    {"type": "matn",
     "ar": "ولهذا لم يعرفه على حدة روما للاختصار",
     "en": "for this reason he did not define it separately, aiming at brevity."},
    {"type": "matn",
     "ar": "(منصوب وجوبا إذا كان) واقعا (بعد «إلا») لا بعد «غير وسوى» وغيرهما (غير الصفة) قيد به، وإن لم يكن الواقع بعد «إلا» التي للصفة داخلا في المستثنى لئلا يذهل عنه",
     "en": "(is necessarily in the accusative when it) occurs (after “illā”), not after “ghayr” and “siwā” and the like, ([illā] other than the adjectival one); he added this restriction, even though what occurs after the “illā” that serves as an adjective is not included in the excepted term, so that it would not be overlooked,"},
    {"type": "matn",
     "ar": "(في كلام موجب) أي: ليس بنفي[[١]] ولا نهي ولا استفهام، نحو: «جاءني القوم إلا زيدا».",
     "en": "(in affirmative speech—kalām mūjab), that is, [speech that] is not a negation, a prohibition or a question, as in “The people came to me except Zayd.”"},
    {"type": "matn",
     "ar": "واحترز به عما إذا وقع في كلام غير موجب؛ لأنه ليس حينئذ واجب النصب على ما سيجيء،",
     "en": "By this he excluded the case where it occurs in non-affirmative speech, because it is not then necessarily in the accusative, as will come."},
    {"type": "matn",
     "ar": "ولا حاجة ههنا إلى قيد آخر، وهو أن يكون الكلام الموجب تاما[[٢]] بأن يكون[[٣]] المستثنى منه مذكورا فيه، ليخرج نحو: «قرأت إلا يوم كذا»، فإنه منصوب على الظرفية لا على الاستثنائية[[٤]]؛",
     "en": "There is no need here for a further restriction, namely that the affirmative speech be complete (tāmm), in that the term from which the exception is made (mustathnā minhu) is mentioned in it, so as to exclude such as “I read except on such-and-such a day”; for that is in the accusative as an adverb of time (ẓarf), not as an exception;"},
    {"type": "matn",
     "ar": "لأن الكلام في كونه منصوبا مطلقا[[٥]]، لا في كونه منصوبا على الاستثناء بدليل قوله: «أو كان بعد خلا وعدا»",
     "en": "because the discussion concerns its being in the accusative absolutely, not its being in the accusative as an exception, as is shown by his words “or it comes after khalā and ʿadā.”"},
    {"type": "matn",
     "ar": "إلا أن يقال: الحاجة إلى هذا القيد إنما هو لإخراج مثل: «قرئ إلا يوم كذا»، فإنه مرفوع وجوبا لا منصوب.",
     "en": "Unless it is said: the need for this restriction is only to exclude such as “It was read except on such-and-such a day,” for that is necessarily in the nominative, not the accusative."},
    {"type": "matn",
     "ar": "والعامل في نصب المستثنى[[٦]] إذا كان منصوبا على الاستثناء عند البصريين الفعل المتقدم، أو معنى الفعل بتوسط «إلا»[[٧]]؛",
     "en": "The governor (ʿāmil) of the accusative in the excepted term, when it is in the accusative as an exception, is according to the Baṣrans the preceding verb, or the sense of the verb, through the mediation of “illā”;"},
    {"type": "matn",
     "ar": "لأنه شيء يتعلق بالفعل أو معناه تعلقا معنويا؛ إذ له نسبة إلى ما نسب إليه أحدهما، وقد جاء بعد تمام الكلام، فشابه المفعول.",
     "en": "because it is something connected to the verb or its sense by a semantic connection, since it has a relation to that to which one of the two is attributed, and it comes after the speech is complete; so it resembles the object (mafʿūl)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الموجب والمثبت اصطلاحا ما ذكره. وغير الموجب وغير المثبت اصطلاحا ما يقابله.",
     "en": "The affirmative (mūjab) and the positive (muthbat), as technical terms, are what he mentioned; and the non-affirmative and non-positive, as technical terms, are what stands opposite it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الكلام التام اصطلاحا في باب الاستثناء ما فسره بقوله: بأن يكون إلى آخره، والكلام الناقص اصطلاحا في هذا الباب ما يقابله.",
     "en": "Complete speech (al-kalām al-tāmm), as a technical term in the chapter on exception, is what he explained by his words “in that … is …” to the end; and incomplete speech (al-kalām al-nāqiṣ), as a technical term in this chapter, is what stands opposite it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قوله: بأن يكون تفسير لما اصطلح عليه في الكلام التام في باب المستثنى، ويسمى ما يقابله كلاما ناقصا.",
     "en": "His words “in that … is” are an explanation of what was agreed as the technical sense of complete speech in the chapter on the excepted term; and what stands opposite it is called incomplete speech."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لعل المعترض أراد بذلك أنه من قبيل المفرغ، فينبغي أن يكون داخلا في الآتي.",
     "en": "Perhaps the objector meant by this that it belongs to the class of the emptied [exception] (mufarragh), so it ought to fall under what comes [later]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الظاهر أن الكلام في كونه منصوبا بنصب استحقه لذاته لا لكونه نائبا مناب المستثنى منه، فحينئذ لا بد من قيد تام ليتم الضابطة.",
     "en": "What is apparent is that the discussion concerns its being in the accusative by an accusative it merits in itself, not by its standing in place of the mustathnā minhu; in that case the restriction “complete” is indispensable for the rule to be complete."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: قال المصنف في شرح المفصل: العامل فيه المستثنى منه بواسطة «إلا».",
     "en": "Shaykh al-Raḍī said: the author said in Sharḥ al-Mufaṣṣal: its governor is the mustathnā minhu through the mediation of “illā.”"},
    {"type": "pair",
     "ar": "قال: لأنه ربما لا يكون هناك فعل ولا معناه نحو: «القوم إلا زيدا إخوتك».",
     "en": "He said: because there may be no verb there, nor its sense, as in “The people, except Zayd, are your brothers.”"},
    {"type": "pair",
     "ar": "وللبصرية أن يقولوا: إن في الإخوة معنى فعليا، وهو الانتساب بالإخوة",
     "en": "The Baṣrans may reply that in “brotherhood” there is a verbal sense, namely being related by brotherhood."},
    {"type": "pair",
     "ar": "ثم قال: لو لم يكن في الجملة معنى الفعل لجاز أن ينتصب المستثنى.",
     "en": "Then he said: even if there were no sense of the verb in the sentence, it would be permissible for the excepted term to be in the accusative."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "نقضه المصنف بقولنا: القوم إخوتك إلا زيدا.",
     "en": "The author refuted it with our saying: “The people are your brothers, except Zayd.”"},
    {"type": "pair",
     "ar": "ولعل الشارح لم يلتفت لعدم وثوقه على المثال، وجواز أن يكون مصنوعا.",
     "en": "Perhaps the commentator paid no attention [to this] because he did not rely on the example, and because it may be fabricated."},
]
