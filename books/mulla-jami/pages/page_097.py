# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 97 (printed ٩٦)."""

PAGE_NUMBER = 97
PRINTED_PAGE = "٩٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The main text (matn) ----------------
    {"type": "matn",
     "ar": "أفعل» إن كانت صفة[[١]] أن تجمع على «فعل» كـ«حمراء» على «حمر»، وإن كانت اسما أن تجمع على «فعالى» أو «فعلاوات» كـ«صحراء» على «صحارى» أو «صحراوات»،",
     "en": "…afʿal”: if it is an adjective, it is that it be pluralized on the pattern fuʿl — like ḥamrāʾ → ḥumr; and if it is a noun, that it be pluralized on the pattern faʿālā or faʿlāwāt — like ṣaḥrāʾ → ṣaḥārā or ṣaḥrāwāt;"},
    {"type": "matn",
     "ar": "فأصلها: إما «جمع»، أو «جماعى»، أو «جمعاوات»[[٢]]، فإذا اعتبر إخراجها عن واحدة منها تحقق العدل، فأحد السببين فيها العدل التحقيقي، والآخر الصفة الأصلية،",
     "en": "so their base form is either jumaʿ, or jamāʿā, or jamʿāwāt; then when their being drawn out of one of these is taken into account, deviation (ʿadl) is realized. Thus one of the two causes [of diptosis] in them is actual deviation (al-ʿadl al-taḥqīqī), and the other is the original adjectival status (al-ṣifa al-aṣliyya)."},
    {"type": "matn",
     "ar": "وإن صارت بالغلبة في باب التأكيد اسما، وفي «أجمع» وأخواته أحد السببين: وزن الفعل، والآخر: الصفة الأصلية.",
     "en": "even though, by predominance, it became a noun in the chapter of corroboration (tawkīd). In “ajmaʿ” and its sisters, one of the two causes is the verbal pattern (wazn al-fiʿl), and the other is the original adjectival status."},
    {"type": "matn",
     "ar": "وعلى ما ذكرناه[[٣]] لا يرد الجموع الشاذة، كـ«أنيب، وأقوس»،",
     "en": "According to what we have stated, the anomalous plurals — like anyub and aqwus — do not constitute an objection,"},
    {"type": "matn",
     "ar": "فإنه لم يعتبر إخراجهما عما هو القياس فيهما، كـ«الأنياب والأقواس» كيف ولو اعتبر جمعهما أولا على «أنياب وأقواس»، فلا شذوذ في هذه الجمعية،",
     "en": "for what was reckoned was not their being drawn out of what is analogically standard in them — like al-anyāb and al-aqwās. How so, when, even if their plural were first reckoned as anyāb and aqwās, there would be no anomaly in this pluralization?"},
    {"type": "matn",
     "ar": "ولا قاعدة للاسم المخرج من مخالفتها الشذوذ[[٤]]، فمن أين يحكم فيهما بالشذوذ؟ ومن هذا تبين الفرق بين الشاذ والمعدول.",
     "en": "and there is no rule for the drawn-out noun such that its diverging [from it] would be anomalous. So on what basis would anomaly be adjudged in the two? From this the distinction between the anomalous (al-shādhdh) and the deviated (al-maʿdūl) has become clear."},
    {"type": "matn",
     "ar": "(أو تقديرا) أي: خروجا كائنا عن أصل مقدر مفروض يكون الداعي إلى تقديره، وفرضه منع الصرف لا غير (ك«عمر»[[٥]]) وكذلك زفر،",
     "en": "(“Or by supposition [taqdīran]”) — that is, a departure occurring from a supposed, posited base, the motive for supposing and positing which is diptosis (man‘ al-ṣarf) and nothing else — (“like ‘ʿUmar’ ”), and likewise Zufar."},
    {"type": "matn",
     "ar": "فإنهما لما وجدا غير منصرفين، ولم يوجد فيهما سبب ظاهر، إلا العلمية اعتبر فيهما العدل،",
     "en": "For since the two are found to be non-triptotic (diptote) while no manifest cause is present in them except proper-namehood (ʿalamiyya), deviation was reckoned in them;"},
    {"type": "matn",
     "ar": "ولما توقف اعتبار العدل على وجود الأصل، ولم يكن فيهما دليل على وجوده غير منع الصرف قدر فيهما أن أصلهما «عامر وزافر» عدل عنهما إلى «عمر وزفر».",
     "en": "and since the reckoning of deviation depends on the existence of a base, and there was in them no evidence for its existence other than diptosis, it was supposed in them that their base is ʿĀmir and Zāfir, deviated from to ʿUmar and Zufar."},
    {"type": "matn",
     "ar": "(و) مثل: (باب قطام) المعدولة عن «قاطمة»، وأراد ببابها: كل ما هو على «فعال» علما للأعيان المؤنثة من غير ذوات الراء (في) لغة (بني تميم)، فإنهم[[٦]] اعتبروا العدل",
     "en": "(“And”) [an example is] (“the category of Qaṭāmi”), deviated from “Qāṭima.” By “its category” he means every word of the pattern faʿāl serving as a proper name for feminine individuals, other than those ending in rāʾ, (“in”) the dialect of (“the Banū Tamīm”); for they reckoned deviation…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "عليه الأكثرون. واعترض عليه بأن فعلاء إنما يجمع على فعل إذا كان مذكره مجموعا على فعل أيضا.",
     "en": "The majority hold this. It has been objected against him that faʿlāʾ is pluralized on the pattern fuʿl only when its masculine [counterpart] is likewise pluralized on the pattern fuʿl."},
    {"type": "pair",
     "ar": "وأجمع مجموع على أجمعون لا على جمع.",
     "en": "But ajmaʿ is pluralized as ajmaʿūn, not as jumaʿ."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال بعض المحققين: لا يخفى أن القياس في جمع التكثير الذي هو جمع ليس جمعاوات، فلا يحتمل أن يكون معدولا عنها، انتهى.",
     "en": "One of the verifying scholars said: it is not hidden that the analogically standard plural of multiplicity for “jamʿ” is not jamʿāwāt, so it cannot be that [jumaʿ] is deviated from it. End [of quotation]."},
    {"type": "pair",
     "ar": "ويمكن أن يقال: لا مانع من اعتبار عدوله عن الجمع السالم وإن كان صورته يشبه الجمع المكسر.",
     "en": "It may be said [in reply]: there is nothing to prevent reckoning its deviation from the sound plural (al-jamʿ al-sālim), even though its form resembles the broken plural (al-jamʿ al-mukassar)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "من تفسير معنى الخروج عن الصيغة الأصلية، وتبيينه بالأمثلة لا يرد الجموع الشاذة، أي: لا ينتقض التفسير بها.",
     "en": "From the explanation of the meaning of departure from the original form and its clarification by examples, the anomalous plurals raise no objection — that is, the explanation is not invalidated by them."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فلا يثبت الشذوذ في أقوس لا باعتبار كونه جمع قوس؛ لأن الجمع أقواس لا أقوس، ولا باعتبار عدوله عن أقواس لعدم تصور الشذوذ في المعدول.",
     "en": "So anomaly is not established in aqwus — neither by reason of its being the plural of qaws, since the plural is aqwās, not aqwus; nor by reason of its being deviated from aqwās, since no anomaly is conceivable in what is deviated."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "خبر مبتدأ محذوف أي: ذلك الخروج كخروج عمر، أو صفة بعد صفة لـ«خروجا» أي: خروجا كائنا عن أصل مقدر مثل: خروج عمر.",
     "en": "[It is] the predicate of an omitted subject — that is: “that departure is like the departure of ʿUmar”; or it is an adjective following an adjective qualifying “departure” — that is: “a departure occurring from a supposed base, like the departure of ʿUmar.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: بني تميم أو النحاة في لغتهم.",
     "en": "That is: the Banū Tamīm, or the grammarians [describing] their dialect."},
]
