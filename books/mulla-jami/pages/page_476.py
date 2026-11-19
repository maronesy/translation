# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 476 (printed ٤٧٥)."""

PAGE_NUMBER = 476
PRINTED_PAGE = "٤٧٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… من حيث إنه اسم تفضيل» at the foot of PDF p. 475 (the line ends there; this page opens indented).
    {"type": "matn",
     "ar": "فيه معنى الفعلية، وذلك المعمول قوله: «منه في عين زيد» (بأجنبي[[١]]، وهو الكحل)؛",
     "en": "…containing the meaning of the verb; that governed element is his words “than it is in the eye of Zayd”, (by a foreign element, namely the kohl);"},
    {"type": "matn",
     "ar": "إذ كل ما ليس معمولا له من هذه الحيثية[[٢]]، فهو أجنبي له من هذه الحيثية، لا يجوز تخلله بينه وبين معمولاته من هذه الحيثية،",
     "en": "for everything that is not governed by it in this respect is foreign to it in this respect, and may not intervene between it and what it governs in this respect;"},
    {"type": "matn",
     "ar": "ولا يخرجه عن هذه الأجنبية ما عرض له من معنى الابتداء، العامل في المبتدأ والخبر؛",
     "en": "and what befalls it of the meaning of inception (ibtidāʾ), the governor of the mubtadaʾ and the khabar, does not remove it from this foreignness,"},
    {"type": "matn",
     "ar": "إذ العامل في الحقيقة حينئذ معنى الابتداء لا اسم التفضيل،",
     "en": "since the real governor in that case is the meaning of inception, not the elative;"},
    {"type": "matn",
     "ar": "بخلاف ما إذا عمل في الكحل بالفاعلية، فإنه لم يبق أجنبيا حينئذ، فإنه من معمولاته من حيث إنه اسم تفضيل،",
     "en": "unlike when it governs the kohl as agent, for then it no longer remains foreign, since it is among what it governs insofar as it is an elative."},
    {"type": "matn",
     "ar": "ولو قدم[[٣]] قوله: «منه في عين زيد» على «الكحل»[[٤]] لم يلزم الفصل بين أحسن ومعموله من حيث إنه اسم تفضيل،",
     "en": "Had his words “than it is in the eye of Zayd” been put before “the kohl”, no separation would follow between aḥsan and what it governs insofar as it is an elative;"},
    {"type": "matn",
     "ar": "ولكن في معناه تعقيد ركيك[[٥]]،",
     "en": "but there is a feeble complexity (taʿqīd) in its meaning."},
    {"type": "matn",
     "ar": "وكذا لو قيل بهذه العبارة: «ما رأيت رجلا أحسن من الكحل في عينه هو -أي: الكحل- في عين زيد» لا يخلو عن ركاكة وتعقيد أيضا،",
     "en": "Likewise, if it were said in this expression, “I have not seen a man in whose eye kohl is more beautiful than it — that is, the kohl — is in the eye of Zayd”, it would not be free of feebleness and complexity either;"},
    {"type": "matn",
     "ar": "مع أنهما ليسا من قبيل العبارة المشهورة[[٦]] الواردة في أداء مثل هذا المقصود والكلام فيها،",
     "en": "besides which, neither belongs to the well-known expression that occurs for conveying such an intended meaning, and the discussion concerns that [expression]."},
    {"type": "matn",
     "ar": "ولما قرر مسألة الكحل[[٧]]، وبين شرائطها[[٨]]، وما",
     "en": "Having established the kohl question and explained its conditions, and what…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لم يقل: لفصلوا بين العامل ومعموله بأجنبي؛ لأن الفصل بين العامل والمعمول لا يمتنع بل بين أفعل ومعموله لضعف عمله،",
     "en": "He did not say “they would have separated between the governor and what it governs by a foreign element”, because separation between a governor and what it governs is not prohibited [in general], but only between afʿal and what it governs, owing to the weakness of its government;"},
    {"type": "pair",
     "ar": "فيجوز زيدا كان عمرو ضاربا، نص عليه الرضي.",
     "en": "so “Zayd, ʿAmr was striking” is permissible; al-Raḍī stated this explicitly."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: من حيث إنه اسم تفضيل فيه معنى الفعلية سواء كان معمولا له باعتبار الزيادة، أو باعتبار معنى الفعل.",
     "en": "That is, insofar as it is an elative containing the meaning of the verb, whether governed by it in regard to excess or in regard to the meaning of the verb."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "بأن يقال: رأيته رجلا أحسن في عينه منه الكحل في عين زيد.",
     "en": "By saying: “I saw him a man in whose eye, than it [is] in the eye of Zayd, the kohl is more beautiful.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إشارة إلى شبهة نقلت عن المصنف من أنه فليقدم منه على الكحل حتى لا يلزم الفصل بين العامل والمعمول،",
     "en": "An allusion to a difficulty reported from the author: that “minhu” should then be put before “the kohl”, so that no separation between governor and governed follows."},
    {"type": "pair",
     "ar": "ولم يلتفت إلى جواب نقل عنه، وهو أنه لو قدم لزم عود الضمير إلى ما لم يذكر؛",
     "en": "He paid no attention to a reply reported from him, namely that if it were put first, the pronoun would refer to what has not been mentioned,"},
    {"type": "pair",
     "ar": "لأنه رده الهندي بأنه لا فساد في رجع الضمير إلى ما لم يذكر لفظا، وهو مذكور رتبة، كما في هذا المثال؛",
     "en": "because al-Hindī rejected it, [saying] that there is nothing wrong in a pronoun referring to what is not mentioned in wording while it is mentioned in rank, as in this example,"},
    {"type": "pair",
     "ar": "لأن الكحل المؤخر لكونه مبتدأ مقدم رتبة. وأجاب بأنه تعقيد ركيك، فرجح العمل مع ضعف عمله عليه.",
     "en": "since the kohl placed later, being a mubtadaʾ, comes first in rank. He replied that it is a feeble complexity, and so he preferred government, despite the weakness of its government, over it."},
    {"type": "pair",
     "ar": "ويمكن أن يجعل ما ذكره المصنف راجعا إلى ما ذكره، يعني: يلزم رجع الضمير إلى ما لم يذكر لفظا، فيكون فيه تعقيد،",
     "en": "It is possible to take what the author mentioned as reducing to what he [al-Hindī] mentioned, meaning: the pronoun would refer to what is not mentioned in wording, so there would be complexity in it;"},
    {"type": "pair",
     "ar": "ويمكن أن يجعل جوابه تحريرا لما ذكره المصنف، فانظر أطراف الكلام، لئلا تكون بالتقصير الملام على فوت المرام.",
     "en": "and it is possible to take his reply as a precise statement of what the author mentioned. So consider the sides of the discussion, lest you be the one blamed, through falling short, for missing the aim."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لأن فيه ذكر اسم التفضيل والمفضل عليه قبل ذكر المفضل، وهو يوجب التعقيد في اللفظ، والركاكة في المعنى.",
     "en": "Because in it the elative and the one surpassed are mentioned before the one preferred is mentioned, which entails complexity in the wording and feebleness in the meaning."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يعني: أن المدعى أن العبارة المشهورة فيها إعمال اسم التفضيل في المظهر؛ إذ لو لم يعمل في المظهر يلزم الفصل بين اسم التفضيل ومعموله بالأجنبي، لا في كل عبارة تؤدي معناه، فتدبر.",
     "en": "He means: what is claimed is that in the well-known expression the elative governs the explicit noun, since if it did not govern the explicit noun a separation between the elative and what it governs by a foreign element would follow; not in every expression that conveys its meaning. Ponder this."},
    {"type": "pair",
     "ar": "فإنه مع وضوحه قد خفي على البعض، فقال ما قال.",
     "en": "For, clear as it is, it has escaped some, who then said what they said."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: مسألة عمل اسم التفضيل الرفع في المظهر، فالإضافة لأدنى ملابسة.",
     "en": "That is, the question of the elative governing the nominative in an explicit noun; so the annexation [“the kohl question”] is by the slightest connection."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "الثلاث، وهو أن يكون الوصف سببا، والتغاير بين المفضل والمفضل عليه اعتباريا، وكونه منفيا.",
     "en": "The three: that the qualification be causal (sababī), that the difference between the one preferred and the one surpassed be by consideration, and that it be negated."},
]
