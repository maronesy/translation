# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 513 (printed ٥١٢)."""

PAGE_NUMBER = 513
PRINTED_PAGE = "٥١٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «على تقدير الإلغاء، وجعلهما» at the foot of PDF p. 512 (mid-sentence).
    {"type": "matn",
     "ar": "مبتدأ وخبرا مع ضعف عملها بالتوسط أو التأخر،",
     "en": "…a subject and a predicate, given the weakness of their government through being placed in the middle or after."},
    {"type": "matn",
     "ar": "وقد نقل الإلغاء عند التقديم[[١]] أيضا نحو: «ظننت زيد قائم» لكن الجمهور على أنه لا يجوز[[٢]]،",
     "en": "Cancellation has also been transmitted when [the verb] is placed first, as in “ẓanantu Zaydun qāʾimun”; but the majority hold that it is not permitted."},
    {"type": "matn",
     "ar": "وهذه الأفعال على تقدير إلغائها في معنى الظروف، فمعنى «زيد قائم ظننت»: زيد قائم في ظني.",
     "en": "On the supposition of their cancellation, these verbs are in the sense of adverbials; so the meaning of “Zaydun qāʾimun ẓanantu” is “Zayd is standing, in my supposition”."},
    {"type": "matn",
     "ar": "وفي قوله: «جواز الإلغاء» إشارة إلى جواز إعمالها أيضا على تقدير التوسط والتأخر.",
     "en": "In his words “the permissibility of cancellation” there is an indication that giving them government is also permitted when they are placed in the middle or after."},
    {"type": "matn",
     "ar": "وفي بعض الشروح: أن الإعمال أولى على تقدير التوسط.",
     "en": "In some commentaries: giving government is preferable when [the verb] is placed in the middle."},
    {"type": "matn",
     "ar": "وفي بعضها: أنهما متساويان[[٣]] والإلغاء أولى على تقدير التأخر.",
     "en": "In others: the two are equal [then], and cancellation is preferable when it is placed after."},
    {"type": "matn",
     "ar": "وقد يقع الإلغاء فيها إذا توسطت بين الفعل ومرفوعه نحو: «ضرب أحسب زيد» وبين اسم الفاعل ومعموله نحو: «لست بمكرم أحسب زيدا»",
     "en": "Cancellation occurs in them when they are placed between the verb and its nominative, as in “ḍaraba aḥsabu Zaydun” (Zayd, I reckon, struck); between the active participle and what it governs, as in “lastu bi-mukrimin aḥsabu Zaydan” (I am not, I reckon, honouring Zayd);"},
    {"type": "matn",
     "ar": "وبين معمولي «إن» نحو: «إن زيدا أحسب قائم»، وبين «سوف» ومصحوبها نحو: «سوف أحسب يقوم زيد»، وبين المعطوف والمعطوف عليه نحو: «جاءني زيد وأحسب عمرو»،",
     "en": "between the two terms governed by “inna”, as in “inna Zaydan aḥsabu qāʾimun” (Zayd, I reckon, is standing); between “sawfa” and what accompanies it, as in “sawfa aḥsabu yaqūmu Zaydun” (Zayd, I reckon, will stand); and between the coordinated term and that to which it is coordinated, as in “jāʾanī Zaydun wa-aḥsabu ʿAmrun” (Zayd came to me and, I reckon, ʿAmr)."},
    {"type": "matn",
     "ar": "ولا شك أن إلغاءها في هذه الصور واجب، فلهذا قيد[[٤]] جوازه المنبيء[[٥]] عن جواز الإعمال أيضا بقوله: «إذا توسطت –يعني: بين معموليها- أو تأخرت يعني: عنهما»",
     "en": "There is no doubt that their cancellation in these cases is obligatory; it is for this reason that he qualified its permissibility, which indicates that giving government is also permitted, by his words “when they are placed in the middle”, meaning between their two objects, “or after”, meaning after them both."},
    # REVIEW: printed «هذه الإلغاء» (feminine demonstrative with a masculine noun); transcribed as printed. Also the matn prints «المنبيء» while footnote ٥ prints «المنبئ»; each transcribed as printed.
    {"type": "matn",
     "ar": "وإنما خص هذه الإلغاء الخاص بالذكر مع أن مطلقه أيضا من خصائصها لشيوعه وكثرة وقوعه.",
     "en": "He singled out this particular cancellation for mention, although cancellation in general is also among their particular properties, only because it is widespread and occurs frequently."},
    {"type": "matn",
     "ar": "(ومنها) أي: من خصائص أفعال القلوب (أنها تعلق) وتعليقها وجوب إبطال عملها لفظا دون معنى بسبب وقوعها (قبل) معنى (الاستفهام[[٦]]) بلا واسطة -كما",
     "en": "(And among them), that is, among the particular properties of the verbs of the heart, (is that they are suspended); their suspension (taʿlīq) is the obligatory annulment of their government in wording but not in meaning, because they occur (before) the sense of (interrogation) without intermediary, as…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لأن أفعال القلوب ضعيفة؛ إذ ليس تأثيرها كالعلاج، وأيضا معمولها في الحقيقة مضمون الجملة لا الجملة.",
     "en": "Because the verbs of the heart are weak, since their effect is not like a physical action; moreover, what they govern is in reality the content of the sentence, not the sentence."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «وعامل لنصب» (without the article), apparently for «وعامل النصب»; transcribed as printed.
    {"type": "pair",
     "ar": "لأن عامل الرفع معنوي عند النحاة، وعامل لنصب لفظي، فمع تقدمها يغلب اللفظي المعنوي.",
     "en": "Because the governor of the nominative is, according to the grammarians, an abstract one, while the governor of the accusative is a verbal one; so when [the verb] comes first, the verbal [governor] prevails over the abstract one."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن العامل القوي أعني: فعل القلب تقدم على أحدهما وتأخر عن الآخر.",
     "en": "Because the strong governor, namely the verb of the heart, comes before one of them and after the other."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "تقديم الجار والمجرور لمجرد الاهتمام والاعتناء بشأن العلة لا للحصر أي: لأجل إخراج هذه الصور قيد الجواز بالتوسط المخصوص أعني: بين المفعولين.",
     "en": "Putting the preposition and its object first is merely for emphasis and attention to the matter of the reason, not for restriction; that is, it is in order to exclude these cases that he qualified the permissibility by the specific placing in the middle, namely between the two objects."},
    {"type": "pair",
     "ar": "وأما التقييد بمطلق التوسط فلإخراج صورة التقدم.",
     "en": "As for the qualification by placing in the middle in general, it is to exclude the case of being placed first."},
    {"type": "pair",
     "ar": "فإن قلت: إن المصنف لم يقيد التوسط بكونه بين المفعولين والتأخر بكونه عنهما؟",
     "en": "If you say: the author did not qualify placing in the middle as being between the two objects, nor placing after as being after them?"},
    {"type": "pair",
     "ar": "قلت: ذلك مستفاد من السوق؛ لأن كلامنا في المفعولين.",
     "en": "I say: that is understood from the course of the discussion, because our discussion concerns the two objects."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بناء على المعنى المتبادر منه، وإنما قال: المنبئ لجواز حمل الجواز على ما يشمل الوجوب وترك التوسط والتأخر على العموم.",
     "en": "On the basis of the sense that first comes to mind from it. He said “which indicates” only because it is possible to take “permissibility” in a sense that includes obligation, and to leave “placing in the middle” and “placing after” in their general sense."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سواء كان في قالب الحرف أو في قالب الاسم، نحو قوله تعالى: ﴿لنعلم أي الحزبين أحصى﴾ (الكهف:١٢)",
     "en": "Whether it is in the form of a particle or in the form of a noun, as in His words, the Exalted: “that We might know which of the two parties best calculated” (Qurʾān, Sūrat al-Kahf 18:12)."},
    {"type": "pair",
     "ar": "وللتنبيه على العموم زاد لفظ المعنى.",
     "en": "To draw attention to this generality he added the word “sense”."},
]
