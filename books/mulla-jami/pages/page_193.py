# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 193 (printed ١٩٢)."""

PAGE_NUMBER = 193
PRINTED_PAGE = "١٩٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # continues from page 192 ("…مصدر وقع مضمون")
    {"type": "matn",
     "ar": "جملة، وهي: «له علي ألف درهم»[[١]]؛ لأن مضمونه الاعتراف، ولا محتمل لها سواه.",
     "en": "…of a sentence, namely: “He has a claim on me of a thousand dirhams”; because its content is acknowledgment, and it has no possible [sense] other than that."},
    {"type": "matn",
     "ar": "(ويسمى[[٢]]) هذا النوع من المفعول المطلق (تأكيدا لنفسه) أي: نفس المفعول المطلق؛",
     "en": "(And) this kind of absolute object (is called “emphasis of itself”—taʾkīdan li-nafsihi), that is, of the absolute object itself;"},
    {"type": "matn",
     "ar": "لأنه إنما يؤكد نفسه وذاته[[٣]]، لا أمرا يغايره ولو بالاعتبار.",
     "en": "because it emphasizes only itself and its own essence, not a thing distinct from it, even if only in consideration (bi-l-iʿtibār)."},
    {"type": "matn",
     "ar": "(ومنها: ما وقع مضمون جملة لها) أي: لهذه الجملة (محتمل غيره[[٤]]) أي: غير المفعول المطلق",
     "en": "(And among them is what occurs as the content of a sentence which has)—that is, this sentence has—(a possible [sense] other than it), that is, other than the absolute object,"},
    {"type": "matn",
     "ar": "(نحو: زيد قائم حقا) أي: حق حقا من «حق يحق» إذا ثبت[[٥]] ووجب،",
     "en": "(as in: “Zayd is standing, truly”—Zaydun qāʾimun ḥaqqan), that is: “it is true, truly,” from “ḥaqqa yaḥiqqu,” when a thing is established and binding."},
    {"type": "matn",
     "ar": "فـ«حقا» مصدر وقع مضمون جملة، وهي قوله: «زيد قائم» ولها محتمل غيره؛ لأنها تحتمل الصدق والكذب والحق والباطل.",
     "en": "So “ḥaqqan” is a maṣdar occurring as the content of a sentence, namely his words “Zayd is standing,” and it has a possible [sense] other than it, because it admits truth and falsehood, the true and the false."},
    {"type": "matn",
     "ar": "(ويسمى[[٦]]) هذا النوع من المفعول المطلق (تأكيدا لغيره)؛",
     "en": "(And) this kind of absolute object (is called “emphasis of another”—taʾkīdan li-ghayrihi);"},
    {"type": "matn",
     "ar": "لأنه من حيث هو منصوص عليه بلفظ المصدر يؤكد نفسه من حيث هو محتمل الجملة،",
     "en": "because, insofar as it is stated explicitly by the wording of the maṣdar, it emphasizes itself insofar as it is a possible [sense] of the sentence;"},
    {"type": "matn",
     "ar": "فالمؤكد -اسم مفعول- من حيث اعتبار وصف الاحتمال فيه يغاير المؤكد -اسم فاعل- من حيث إنه",
     "en": "so the emphasized (al-muʾakkad, passive participle), in respect of considering the attribute of possibility in it, differs from the emphasizer (al-muʾakkid, active participle) in that it…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا يخفى أن مضمون الجملة على ما ذكره سابقا هو مصدرها المنسوب إلى فاعل أو مفعول،",
     "en": "It is not hidden that the content of the sentence, according to what he stated earlier, is its maṣdar attributed to an agent or a patient;"},
    {"type": "pair",
     "ar": "و«اعترافا» بالنسبة إلى قوله: «له علي ألف درهم» ليس كذلك، ولا حقا في مقابله بالنسبة إلى «زيد قائم» كذلك،",
     "en": "and “iʿtirāfan” in relation to his words “He has a claim on me of a thousand dirhams” is not so, nor likewise is “ḥaqqan,” its counterpart, in relation to “Zayd is standing,”"},
    {"type": "pair",
     "ar": "اللهم إلا أن يقال: إن المصدر المأخوذ من «زيد قائم» هو حقية هذا القول المحتمل، فتأمل.",
     "en": "unless it be said that the maṣdar taken from “Zayd is standing” is the truth (ḥaqqiyya) of this possible statement; so reflect."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: هذه التسمية من المتأخرين.",
     "en": "That is: this naming is from the later [grammarians] (al-mutaʾakhkhirūn)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كما يؤكد «ضربا» في «ضربت ضربا نفسه» إلا أن المؤكد ههنا مضمون المفرد، أعني: الفعل،",
     "en": "Just as “ḍarban” in “ḍarabtu ḍarban” (I struck a striking) emphasizes itself, except that what is emphasized there is the content of a single word, namely the verb,"},
    {"type": "pair",
     "ar": "وفي مسألتنا يؤكد مضمون الجملة الاسمية.",
     "en": "whereas in our case it emphasizes the content of the nominal sentence."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أخرج ما وقع مضمون مفرد سواء كان له احتمال غيره نحو: «رجع القهقري» أو لم يكن نحو: «ضربت ضربا».",
     "en": "He excluded what occurs as the content of a single word, whether it has a possible [sense] other than it, as in “rajaʿa al-qahqarā” (he went back backwards), or not, as in “ḍarabtu ḍarban.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يجوز أيضا أن يكون من حق الأمر بمعنى تحققه، وكان منه على يقين،",
     "en": "It may also be from “ḥaqqa al-amra” in the sense of “he verified it” and was certain of it;"},
    {"type": "pair",
     "ar": "فالمقصود حينئذ إثبات كونه على يقين، ودفع كونه على شك، فإنه من محتملات الجملة كما أن الباطل والكذب من محتملاتها.",
     "en": "the intent is then to affirm that he is certain and to rule out that he is in doubt, for that is among the possible [senses] of the sentence, just as the false and the untrue are among its possible [senses]."},
    {"type": "pair",
     "ar": "ويجوز أن يكون صفة مصدر محذوف أي: قولا حقا",
     "en": "It may also be the qualifier of an elided maṣdar, that is: “a true statement” (qawlan ḥaqqan),"},
    {"type": "pair",
     "ar": "كما قاله الشيخ الرضي من أن جميع الأمثلة الموردة للمؤكد بغيره: إما صريح القول أو ما في معنى القول",
     "en": "as Shaykh al-Raḍī said, namely that all the examples adduced for what is emphasized by another are either an explicit “statement” or what has the sense of a statement."},
    {"type": "quran",
     "ar": "قال الله تعالى: ﴿ذلك عيسى ابن مريم قول الحق الذي فيه يمترون﴾ (سورة مريم: ٣٤)،",
     "en": "Allah the Exalted said: “That is Jesus, son of Mary—the statement of truth about which they dispute” (Qurʾān, Sūrat Maryam 19:34);"},
    {"type": "pair",
     "ar": "ونحو: لأفعلنه البتة، أي: قطعت بالفعل وجزمت به قطعة واحدة ليس فيه تردد",
     "en": "and as in: “I shall certainly do it, absolutely” (la-afʿalannahu al-battata), that is: I have resolved upon the act and determined on it with a single resolve in which there is no wavering,"},
    {"type": "pair",
     "ar": "بحيث أجزم به ثم يبدو لي، ثم أجزم به مرة أخرى، فيكون قطعتان أو أكثر، بل هو قطعة واحدة لا يثنى فيها النظر.",
     "en": "such that I would determine on it, then reconsider, then determine on it another time, so that there would be two resolves or more; rather it is a single resolve in which the matter is not looked at a second time."},
    {"type": "pair",
     "ar": "وكذا قولهم: أفعله البتة أي: جزمت بأن تفعله وقطعت به قطعة، فالبتة بمعنى القول المقطوع به،",
     "en": "Likewise their saying: “Do it, absolutely,” that is: I have determined that you are to do it and resolved upon it with a single resolve; so al-batta means the statement that is resolved upon,"},
    {"type": "pair",
     "ar": "وكان اللام فيها في الأصل للعهد أي: القطعة المعلومة التي لا تردد فيها،",
     "en": "and the lām in it was originally for prior reference (ʿahd), that is: the known resolve in which there is no wavering."},
    {"type": "pair",
     "ar": "فنقول التقدير الأصلي في مثل هذا المصدر أن تجعل الجملة المتقدمة مفعولا به لـ«قلت»، وهذا المصدر مفعولا مطلقا لـ«قلت» بيانا للنوع،",
     "en": "So we say: the original implied construction in a maṣdar such as this is that you make the preceding sentence a direct object of “qultu” (I said), and this maṣdar an absolute object of “qultu,” specifying the kind;"},
    {"type": "pair",
     "ar": "فالقول الناصب مدلول الجملة المتقدمة؛ لأن المتكلم إذا تكلم بجملة فهي مقوله.",
     "en": "so the “saying” that puts it in the accusative is what the preceding sentence signifies, because when a speaker utters a sentence, it is what he says."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "هذا أيضا من المتأخرين.",
     "en": "This too is from the later [grammarians]."},
]
