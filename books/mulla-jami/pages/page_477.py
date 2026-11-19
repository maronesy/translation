# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 477 (printed ٤٧٦)."""

PAGE_NUMBER = 477
PRINTED_PAGE = "٤٧٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… ولما قرر مسألة الكحل، وبين شرائطها، وما» at the foot of PDF p. 476.
    {"type": "matn",
     "ar": "عبر به عنها[[١]] على وجه يطابق المقصود بلا زيادة ولا نقصان،",
     "en": "…what it is expressed by, in a way that matches the intended meaning with neither excess nor deficiency,"},
    {"type": "matn",
     "ar": "أراد أن ينبه على أن التعبير عنها غير منحصر فيما ذكر، بل يمكن أن يعبر عنها بعبارة أخصر منه، وعلى ترتيب غير ترتيبه،",
     "en": "he wished to point out that its expression is not confined to what was mentioned, but it can be expressed in a wording more concise than that, and in an order other than its order;"},
    {"type": "matn",
     "ar": "وينتقل[[٢]] بهذا التقريب إلى ما أنشده سيبويه، واستشهد به في إثبات هذه المسألة، ويطبق بعض هذه الصور عليه،",
     "en": "and by this approach to pass on to what Sībawayh recited and cited as evidence in establishing this question, and to apply some of these forms to it."},
    {"type": "matn",
     "ar": "فقال: (ولك أن تقول: «ما رأيت رجلا أحسن في عينه الكحل من عين زيد») بإقامة «من عين زيد» مقام «منه في عين زيد»،",
     "en": "So he said: (You may also say “I have not seen a man in whose eye kohl is more beautiful than Zayd’s eye”), by putting “than Zayd’s eye” in place of “than it is in Zayd’s eye”;"},
    {"type": "matn",
     "ar": "وهو أخصر منه بمقدار[[٣]] ضمير «منه»، وكلمة «في»،",
     "en": "this is shorter than it by the amount of the pronoun of “minhu” and the word “fī”."},
    {"type": "matn",
     "ar": "ولو رفع لفظ العين من البين، واكتفى بـ«من زيد» كان أخصر، مع ظهور المعنى المقصود[[٤]]،",
     "en": "Had the word “eye” been removed from the middle, contenting oneself with “than Zayd”, it would have been shorter still, with the intended meaning remaining evident."},
    {"type": "matn",
     "ar": "وعلى كلا التقديرين فالمعنى على ما كان عليه قبل هذا التغيير؛ لأن أصله[[٥]] «من كحل عين زيد»، والمعنى على حذف المضاف،",
     "en": "On both readings the meaning is as it was before this change, because its original form is “than the kohl of Zayd’s eye”, the meaning being with the first term of the annexation elided;"},
    {"type": "matn",
     "ar": "فإنه لو كان كذلك لا يكون من قبيل تفضيل الشيء[[٦]] على نفسه؛ إذ يتعدد الكحل حينئذ.",
     "en": "for if it were so [literally], it would not belong to preferring a thing over itself, since the kohl would then be multiple."},
    {"type": "matn",
     "ar": "(فإن قدمت) على اسم التفضيل (ذكر العين) التي كان الكحل فيها مفضلا عليه",
     "en": "(If you put first), before the elative, (the mention of the eye) in which the kohl was the one surpassed,"},
    {"type": "matn",
     "ar": "(قلت: «ما رأيت كعين زيد أحسن فيها الكحل») كان أصله: «ما رأيت عينا أحسن فيها الكحل منه في عين زيد»",
     "en": "(you say: “I have not seen [an eye] like Zayd’s eye in which kohl is more beautiful”). Its original form was: “I have not seen an eye in which kohl is more beautiful than it is in Zayd’s eye”;"},
    {"type": "matn",
     "ar": "فلما ذكر «عين زيد» مقدما عليه استغنى عن ذكره[[٧]] ثانيا،",
     "en": "when “Zayd’s eye” was mentioned before it, its mention a second time became unnecessary."},
    {"type": "matn",
     "ar": "وتقديره: «ما رأيت[[٨]] عينا ماثلة لعين زيد في أصل التكحل أحسن فيها الكحل من",
     "en": "Its implied form is: “I have not seen an eye resembling Zayd’s eye in the basic application of kohl, in which kohl is more beautiful than…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في استعمالاتهم. وهو قوله: ما رأيت رجلا أحسن في عينه الكحل منه في عين زيد.",
     "en": "In their usages. It is his words “I have not seen a man in whose eye kohl is more beautiful than it is in Zayd’s eye.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: footnote prints «وقوله: تطبيق» while the matn prints «ويطبق»; transcribed as printed in each place.
    {"type": "pair",
     "ar": "عطف على أن ينبه. وقوله: تطبيق إلى آخره عطف على ما أنشده.",
     "en": "Coordinated to “to point out”. His words “applying …” are coordinated to “what he recited”."},
    {"type": "pair",
     "ar": "والإشارة إلى التطبيق حاصل لجعل ما رأيت كعين زيد أحسن فيها الكحل مثل لا أرى إلى آخره.",
     "en": "The allusion to the application results from making “I have not seen [an eye] like Zayd’s eye in which kohl is more beautiful” like “lā arā …”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أشار بزيادة لفظ المقدار إلى أن الاختصار هنا ليس بطريق الحذف، بل بطريق التسامح لظهور المقصود،",
     "en": "By adding the word “amount” he indicated that the abridgement here is not by way of elision but by way of laxity, because the intended meaning is evident;"},
    {"type": "pair",
     "ar": "فلا يرد أن حذف المجرور وإبقاء الجار، وحذف كلمة «في» مع إبقاء مدخوله على الجر لا نظير له في كلام العرب.",
     "en": "so the objection does not arise that eliding the genitive noun while keeping the preposition, and eliding the word “fī” while keeping what it governs in the genitive, has no parallel in the speech of the Arabs."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأن المفضل لا بد أن يكون من جنس المفضل عليه.",
     "en": "Because the one preferred must be of the same genus as the one surpassed."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "حيث قال: وهو على حذف المضاف أي: من كحل عين زيد؛",
     "en": "Since he said: “It is with the first term of the annexation elided, that is, ‘than the kohl of Zayd’s eye’”;"},
    {"type": "pair",
     "ar": "لأنه لتفضيل الكحل على الكحل لا الكحل على العين، و«من» التفضيلية تدخل على المفضول.",
     "en": "because it is for preferring kohl over kohl, not kohl over the eye, and the comparative “min” enters on the one surpassed."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "والحال أن عمل اسم التفضيل في المظهر مشروط بذلك عندهم.",
     "en": "While, in their view, the elative’s government of an explicit noun is conditional on that."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لدلالة قولك كعين زيد عليه؛ لأن معناه كل عين دونها في حسن الكحل فيها.",
     "en": "Because your saying “like Zayd’s eye” indicates it, since its meaning is that every eye is below it in the beauty of kohl in it."},
    {"type": "pair",
     "ar": "وهذا هو المستفاد من ذكر عين زيد بعده، كذا في الرضي.",
     "en": "This is what is conveyed by mentioning Zayd’s eye after it; so in al-Raḍī."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "رد على الرضي حيث قال: لا يجوز أن يكون أحسن فيها الكحل صفة لقولك كعين زيد؛",
     "en": "A rejoinder to al-Raḍī, where he said: “aḥsan fīhā al-kuḥl” cannot be an attribute of your words “like Zayd’s eye”,"},
    {"type": "pair",
     "ar": "لأنه يكون المعنى: ما رأيت مثل عين زيد في حسن الكحل فيها زائدة عليها في حسن الكحل فيها،",
     "en": "because the meaning would be: “I have not seen [an eye] like Zayd’s eye in the beauty of the kohl in it, exceeding it in the beauty of the kohl in it”;"},
    {"type": "pair",
     "ar": "وكيف يكون مثل الشيء في الوصف زائدا عليه في ذلك الوصف في حالة واحدة.",
     "en": "and how can the like of a thing in a quality exceed it in that same quality at one and the same time?"},
]
