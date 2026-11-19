# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 142 (printed ١٤١)."""

PAGE_NUMBER = 142
PRINTED_PAGE = "١٤١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "المعنى يتوجهان إليه[[١]]، ويصح أن يكون هو مع وقوعه في ذلك الموضع[[٢]] معمولا لكل واحد منهما على البدل[[٣]].",
     "en": "…in respect of meaning are directed toward it; and it is valid that it—together with its occurring in that position—be governed by each one of the two [verbs] by way of alternation (ʿalā al-badal)."},
    {"type": "matn",
     "ar": "فحينئذ[[٤]] لا يتصور تنازعهما في الضمير المتصل[[٥]]؛",
     "en": "Accordingly, their contending together is inconceivable in the case of the attached pronoun (al-ḍamīr al-muttaṣil);"},
    {"type": "matn",
     "ar": "لأن المتصل الواقع بعدهما يكون متصلا بالفعل الثاني، وهو مع كونه متصلا بالفعل الثاني لا يجوز أن يكون معمولا للفعل الأول[[٦]]، كما لا يخفى.",
     "en": "because the attached [pronoun] occurring after them is attached to the second verb, and it—along with its being attached to the second verb—cannot be governed by the first verb, as is not hidden."},
    {"type": "matn",
     "ar": "وأما الضمير المنفصل الواقع بعدهما نحو: «ما ضرب وأكرم إلا أنا»[[٧]]، ففيه تنازع، لكن لا يمكن قطعه بما هو طريق القطع عندهم،",
     "en": "As for the detached pronoun occurring after them, as in: “None struck nor honored except I” (mā ḍaraba wa-akrama illā anā), tanāzuʿ [does occur] in it, but its resolution cannot be effected by that which is the method of resolution according to them,"},
    {"type": "matn",
     "ar": "وهو إضمار الفاعل في الأول عند البصريين، وفي الثاني عند الكوفيين؛",
     "en": "which is the concealment of the agent in the first [verb] according to the Baṣrans, and in the second according to the Kūfans;"},
    {"type": "matn",
     "ar": "لأنه لا يمكن إضماره مع «إلا»؛ لأنه حرف لا يصح إضماره ولا بدونه لفساد المعنى؛",
     "en": "because it cannot be concealed together with “illā” (except); for it is a particle whose concealment is not valid, nor [is the utterance valid] without it, on account of the corruption of the meaning [that would ensue];"},
    {"type": "matn",
     "ar": "لأنه يفيد نفي الفعل عن الفاعل، والمقصود إثباته له.",
     "en": "because [dropping it] would convey the negation of the act from the agent, whereas the intent is to affirm it of him."},
    {"type": "matn",
     "ar": "ومراد المصنف بالتنازع[[٨]] ههنا ما يكون طريق قطعه إضمار الفاعل، فلهذا خصه",
     "en": "What the author intends by tanāzuʿ here is that whose method of resolution is the concealment of the agent; and it is for this that he singled it out…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لوقوعه بخصوصه أو بعمومه طرفا لنسبتهما.",
     "en": "Because it occurs—whether specifically or generally—as a term of the [predicative] relation of the two of them."},
    {"type": "pair",
     "ar": "وإنما قلنا بالعموم ليدخل فيه مثل: «حسبني وحسبتهما منطلقين الزيدان منطلقا».",
     "en": "We said “generally” only so that there would be included therein such as: “I deemed [him], and I deemed the two of them, the two Zayds, to be setting off—setting off.”"},
    {"type": "pair",
     "ar": "ولا يخفى أن ذلك التوجيه إما بحسب الأصل والطبع، أو بحسب التصور السابق على التحقيق بمرتبتين؛",
     "en": "It is not hidden that this directing [of the relation] is either in accordance with the origin and [natural] disposition, or in accordance with the conception that precedes actual realization by two ranks;"},
    {"type": "pair",
     "ar": "إذ لا نزاع بالفعل حال تحقق الفعلين لوجدان كل منهما معموله، ولا حال التصور الذي هو مبدأ للتحقق.",
     "en": "for there is no actual contention at the moment the two verbs are realized, since each of them finds its own governed element; nor at the moment of conception, which is the starting point of realization."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لا يأبى من حيث إنه واقع في ذلك الموضع أن يكون معمولا لكل منهما ليتصور النزاع.",
     "en": "That is: it does not refuse—inasmuch as it occurs in that position—to be governed by each of the two, so that contention may be conceivable."},
    {"type": "pair",
     "ar": "ولا يخفى أن منطلقا في «حسبني وحسبتهما منطلقين الزيدان منطلقا» لا يأبى عن وقوعه معمولا للفعل الثاني،",
     "en": "It is not hidden that “munṭaliqan” in “ḥasibnī wa-ḥasibtuhumā munṭaliqīn al-Zaydān munṭaliqan” does not refuse to occur as governed by the second verb;"},
    {"type": "pair",
     "ar": "بل يأبى عن ذلك تثنية المفعول الأول، والتخالف بين المفعولين،",
     "en": "rather, what refuses that is the dualization of the first object and the divergence between the two objects;"},
    {"type": "pair",
     "ar": "وأن الضمير المتصل بالفعل من حيث إنه واقع في ذلك الموضع يأبى عن وقوعه معمولا لغير ذلك الفعل، فظهر الفرق بينهما.",
     "en": "and [note] that the pronoun attached to the verb, inasmuch as it occurs in that position, refuses to occur as governed by other than that verb—so the difference between the two [cases] becomes clear."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: لا على الاجتماع والمعية؛ إذ لا يجوز اجتماع المؤثرين التامين على أثر واحد،",
     "en": "That is: not by way of joint operation and concurrence; for it is not permissible for two complete efficient causes to combine upon a single effect,"},
    {"type": "pair",
     "ar": "وهم يجرون العوامل النحوية مجرى المؤثرات الحقيقية.",
     "en": "and they treat the grammatical governors in the manner of real efficient causes."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: حين إذ كان معنى التنازع في الظاهر ما ذكر، واعتبر فيه صحة كون المتنازع فيه معمولا مع وقوعه في مكانه.",
     "en": "That is: at the time when the meaning of tanāzuʿ in its overt [sense] is what has been mentioned, and there is taken into account in it the validity of the contended-over element’s being governed while occurring in its place."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "مطلقا، أي: سواء كان ضمير غائب أو مخاطب أو متكلم، وسواء كان ضميرا مرفوعا أو غيره.",
     "en": "Absolutely—that is: whether it be a pronoun of the third person (ghāʾib), the second person (mukhāṭab), or the first person (mutakallim), and whether it be a nominative pronoun or otherwise."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إذ لا يطلب فعل أن يكون رافعا لما اتصل بفعل آخر، كما لا يخفى.",
     "en": "For a verb does not demand to be the [nominative] governor of that which is attached to another verb, as is not hidden."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "هذا منقوض بمثل: «أقائم أو قاعد أنت» فإن «قائم» و«قاعد» تنازعا في «أنت».",
     "en": "This is contradicted by such as: “Is standing or sitting—you?” (a-qāʾim aw qāʿid anta), for “qāʾim” and “qāʿid” contend over “anta.”"},
    {"type": "pair",
     "ar": "ويمكن قطع التنازع بالإضمار على مذهب الكوفية والبصرية بلا كلفة.",
     "en": "The tanāzuʿ can be resolved by concealment [of the pronoun] according to the doctrine of the Kūfans and the Baṣrans without difficulty."},
    {"type": "pair",
     "ar": "ولا يخفى عليك أن «قائم» مع استتار فاعله هنا مبتدأ؛ إذ ليس مبتدأ في الكلام حتى يكون خبرا له،",
     "en": "It is not hidden from you that “qāʾim,” along with the concealment of its agent, is here a mubtadaʾ; since it is not [truly] a mubtadaʾ in the discourse such that a khabar would be predicated of it—"},
    {"type": "pair",
     "ar": "فهو صفة واقعة بعد حرف الاستفهام رافعة لغير الظاهر، فينتقض به حد المبتدأ أيضا،",
     "en": "rather it is an adjective occurring after the interrogative particle, functioning as the [nominative] governor of a non-overt [pronoun]—so the definition of the mubtadaʾ is contradicted by it as well;"},
    {"type": "pair",
     "ar": "فليكن هذا على ذكر منك حتى لا تحتاج إلى تنبيه مبتدأ في محله.",
     "en": "so keep this in remembrance, so that you will not need [any further] alerting to a mubtadaʾ in its [proper] place."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لأنه المناسب لما هو بصدده، وذلك لأنه يخالف ما يقتضيه الأصل السابق على رأي البصرية، فاحتيج إلى الاستثناء،",
     "en": "Because it is what is appropriate to what he is engaged in; and that is because it contravenes what the foregoing principle requires according to the view of the Baṣrans, so recourse to an exception (istithnāʾ) was needed,"},
    {"type": "pair",
     "ar": "ويوافقه على رأي الكوفية، فيكون من تفاريع الأصل السابق.",
     "en": "whereas it agrees with it according to the view of the Kūfans, so it is [counted] among the ramifications of the foregoing principle."},
    {"type": "pair",
     "ar": "وأما ذكر المفعول فلتتميم البحث.",
     "en": "As for the mention of the object, it is for the completion of the discussion."},
]
