# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 289 (printed ٢٨٨)."""

PAGE_NUMBER = 289
PRINTED_PAGE = "٢٨٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لجواز أن يكون حينئذ فيهما آلهة غير» from the foot of PDF p. 288.
    {"type": "matn",
     "ar": "مستثنى الله عنها، بخلاف ما إذا كانت للصفة بمعنى «غير»، فإنه يدل على أنه ليس فيهما آلهة غير الله،",
     "en": "…from which God is excepted. It is otherwise when it is an attribute in the sense of “ghayr”: then it indicates that there are not in them gods other than God;"},
    {"type": "matn",
     "ar": "وإذا لم يكن فيهما آلهة غير الله يجب ألا يتعدد الآلهة[[١]]؛ لأن التعدد يستلزم المغايرة.",
     "en": "and if there are not in them gods other than God, the gods cannot be multiple, because multiplicity entails otherness (mughāyara)."},
    {"type": "matn",
     "ar": "(وضعف) حمل «إلا» على «غير» (في غيره) أي: في غير جمع منكور غير محصور لصحة الاستثناء حينئذ.",
     "en": "(And it is weak)—assimilating “illā” to “ghayr”—(in other than it), that is, in other than an indefinite, non-delimited plural, because exception is then valid."},
    {"type": "matn",
     "ar": "ومذهب سيبويه: على جواز وقوع «إلا» صفة مع صحة الاستثناء، قال: يجوز في قولك: «ما أتاني أحد إلا زيد» أن يكون «إلا زيد» صفة،",
     "en": "The doctrine of Sībawayh is that “illā” may occur as an attribute even where exception is valid. He said: in your saying “No one came to me except Zayd,” “illā Zayd” may be an attribute."},
    {"type": "matn",
     "ar": "وعليه أكثر المتأخرين، تمسكا بقوله:",
     "en": "Most of the later [grammarians] hold this, relying on the poet’s words:"},
    {"type": "verse",
     "ar": "وكل أخ مفارقه أخوه          لعمر أبيك إلا الفرقدان[[٢]]",
     "en": "Every brother is parted from by his brother — by your father’s life — except the two Farqads."},
    {"type": "matn",
     "ar": "فـ«إلا الفرقدان» صفة لـ«كل أخ» لا استثناء منه، وإلا لوجب أن يقال: «الفرقدين» بالنصب،",
     "en": "So “illā al-farqadān” is an attribute of “every brother,” not an exception from it; otherwise it would have had to be said “al-farqadayn,” in the accusative."},
    {"type": "matn",
     "ar": "والمصنف حمل ذلك على الشذوذ، وقال في البيت شذوذان آخران:",
     "en": "The author took this as anomalous (shudhūdh), and said that the verse has two further anomalies:"},
    {"type": "matn",
     "ar": "أحدهما: وصف كل دون المضاف إليه، والمشهور وصف المضاف إليه؛ إذ هو المقصود، و«كل» لإفادة الشمول فقط.",
     "en": "the first is qualifying “kull” rather than the noun annexed to it, whereas the usual practice is to qualify the annexed noun, since it is what is intended, “kull” serving only to convey comprehensiveness;"},
    {"type": "matn",
     "ar": "وثانيهما: الفصل بالخبر بين الصفة والموصوف، وهو قليل.",
     "en": "the second is separating the attribute from the qualified noun by the predicate, which is rare."},
    {"type": "matn",
     "ar": "(وإعراب «سوى وسواء» النصب على الظرفية) أي: بناء على ظرفيتهما؛",
     "en": "(The inflection of “siwā” and “sawāʾ” is the accusative as adverbs [ẓarfiyya]), that is, on the basis of their adverbial character;"},
    {"type": "matn",
     "ar": "لأنك إذا قلت: «جاءني القوم سوى أو سواء زيد» فكأنك قلت: «مكان زيد» (على) المذهب (الأصح) وهو مذهب سيبويه، فهما عنده لازم الظرفية.",
     "en": "for when you say “The people came to me, siwā (or sawāʾa) Zayd,” it is as though you said “in place of Zayd”—(on the soundest) doctrine, which is the doctrine of Sībawayh; in his view both are always adverbial."},
    {"type": "matn",
     "ar": "وعند الكوفيين: يجوز خروجهما عن الظرفية، والتصرف فيهما رفعا ونصبا وجرا كـ«غير» متمسكين بقول الشاعر:",
     "en": "According to the Kūfans, they may leave adverbial use and be inflected freely in the nominative, accusative and genitive, like “ghayr,” relying on the poet’s words:"},
    {"type": "verse",
     "ar": "ولم يبق سوى العدوا          ن دناهم كما دانوا",
     "en": "Nothing remained but aggression: we requited them as they had dealt."},
    {"type": "matn",
     "ar": "وزعم الأخفش: أن «سواء» إذا أخرجوه عن الظرفية أيضا نصبوه استنكارا لرفعه،",
     "en": "Al-Akhfash claimed that when they take “sawāʾ” out of adverbial use they still put it in the accusative, finding its nominative objectionable,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: يجب ألا يكون إله إلا الله؛ لأن التعدد يستلزم المغايرة، والمغايرة مستلزمة للفساد،",
     "en": "That is, there must be no god but God; because multiplicity entails otherness, and otherness entails ruin;"},
    {"type": "pair",
     "ar": "وانتفاء اللازم مستلزم لانتفاء الملزومات كلها، كما أن إثبات الملزوم مستلزم إثبات لوازمه كلها.",
     "en": "and the negation of the consequent entails the negation of all its antecedents, just as the affirmation of the antecedent entails the affirmation of all its consequents."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الفرقد ولد البقرة الوحشية. والنجم الذي يهتدى به. وهما فرقدان. وجاء في الشعر مثنى وموحدا، كذا في القاموس.",
     "en": "“Al-farqad” is the calf of the wild cow, and the star by which one is guided; and they are two Farqads. It occurs in poetry in the dual and in the singular; so in al-Qāmūs."},
    {"type": "pair",
     "ar": "وفي الصحاح: الفرقدان نجمان قريبان من القطب.",
     "en": "In al-Ṣiḥāḥ: the two Farqads are two stars near the pole."},
]
