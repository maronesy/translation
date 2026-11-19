# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 337 (printed ٣٣٦)."""

PAGE_NUMBER = 337
PRINTED_PAGE = "٣٣٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(يتوسط بينه)» at the foot of PDF p. 336.
    {"type": "matn",
     "ar": "أي: بين ذلك التابع (وبين متبوعه أحد الحروف العشرة) وسيأتي تفصيلها في قسم الحروف إن شاء الله تعالى.",
     "en": "…that is, between that dependent (and the noun it follows, one of the ten particles); their detailed account will come in the section on particles, if Allah the Exalted wills."},
    {"type": "matn",
     "ar": "(مثل: «قام زيد وعمرو») ولم يكتف بقوله: «تابع يتوسط بينه وبين متبوعه أحد الحروف العشرة»؛",
     "en": "(As in “qāma Zaydun wa-ʿAmrun” [Zayd and ʿAmr stood]). He did not content himself with saying “a dependent between which and the noun it follows one of the ten particles intervenes”,"},
    {"type": "matn",
     "ar": "لأن الحروف قد يتوسط بين الصفات مثل: «جاءني زيد العالم والشاعر والدبير»، فالصفة الداخلة عليها حرف العطف كـ«الشاعر والدبير» لها جهتان:",
     "en": "because the particles sometimes intervene between qualifiers, as in “jāʾanī Zaydun al-ʿālimu wa-l-shāʿiru wa-l-dabīru” (Zayd, the learned, the poet and the prudent, came to me); so a qualifier on which the conjunctive particle enters, such as “al-shāʿir” and “al-dabīr”, has two aspects."},
    {"type": "matn",
     "ar": "إحداهما: كونها صفة لـ«زيد» تابعة له بتبعية المعطوف عليه.",
     "en": "The first: its being a qualifier of “Zayd”, dependent on it through the dependence of the noun conjoined to."},
    {"type": "matn",
     "ar": "وأخراهما: كونها معطوفا على الصفة المتقدمة تابعة لها،",
     "en": "The other: its being conjoined to the preceding qualifier and dependent on it."},
    {"type": "matn",
     "ar": "ويصدق على هذه الصفة من جهتها الأولى أنها تابع؛ لأنها صفة لـ«زيد» يتوسط بينها وبين «زيد» حرف العطف؛",
     "en": "Of this qualifier, in its first aspect, it holds true that it is a dependent between which and “Zayd” the conjunctive particle intervenes, since it is a qualifier of “Zayd”;"},
    {"type": "matn",
     "ar": "لأن توسط حرف العطف بين شيئين لا يلزم أن يكون لعطف الثاني على الأول،",
     "en": "for the intervention of the conjunctive particle between two things need not be for conjoining the second to the first."},
    {"type": "matn",
     "ar": "فلو لم يكن قوله: «مقصود بالنسبة مع متبوعه» لدخل هذه الصفة من جهتها الأولى في حد المعطوف، وهي من هذه الجهة ليست معطوفة، فلم يبق مانعا.",
     "en": "Had his words “intended by the attribution together with the noun it follows” not been there, this qualifier in its first aspect would have entered the definition of the conjoined noun, though in this aspect it is not conjoined; so [the definition] would not have remained exclusive."},
    {"type": "matn",
     "ar": "وقيل: قد جوز الزمخشري[[١]] وقوع الواو بين الصفة والموصوف لتأكيد اللصوق في مواضع عديدة من الكشاف،",
     "en": "It has been said: al-Zamakhsharī permitted the wāw to occur between the qualifier and the qualified noun, to reinforce their adherence (taʾkīd al-luṣūq), in numerous places in al-Kashshāf;"},
    {"type": "matn",
     "ar": "وحكم المصنف في شرح المفصل في مباحث الاستثناء أن قوله تعالى: ﴿ولها منذرون﴾ في قوله تعالى: ﴿وما أهلكنا من قرية إلا لها منذرون﴾[[٢]] صفة لـ«قرية»،",
     "en": "and the author ruled, in his Sharḥ al-Mufaṣṣal in the discussions of exception, that His words, Exalted is He, “wa-lahā mundhirūn” (but it had warners), in His words, Exalted is He, “And We destroyed no town but that it had warners” (Qurʾān, Sūrat al-Shuʿarāʾ 26:208), are a qualifier of “qarya” (town)."},
    # REVIEW: printed «تابع بتوسط» here, whereas the definition elsewhere reads «تابع يتوسط»; transcribed as printed.
    {"type": "matn",
     "ar": "فلو اكتفى بقوله: «تابع بتوسط» لدخل فيه مثل هذه الصفة.",
     "en": "So had he contented himself with saying “a dependent with an intervening [particle]”, such a qualifier as this would have entered it."},
    {"type": "matn",
     "ar": "ونقل عن المصنف[[٣]] أنه قال في أمالي الكافية: إن «العاقل» في مثل: «جاءني زيد العالم والعاقل» تابع يتوسط بينه وبين متبوعه أحد الحروف العشرة، وليس بعطف على التحقيق،",
     "en": "It is reported of the author that he said in his Amālī al-Kāfiya: “al-ʿāqil” in such as “jāʾanī Zaydun al-ʿālimu wa-l-ʿāqilu” (Zayd, the learned and the intelligent, came to me) is a dependent between which and the noun it follows one of the ten particles intervenes, yet in truth it is not a conjunction;"},
    {"type": "matn",
     "ar": "وإنما هو باق على ما كان عليه في الوصفية، وإنما حسن دخول العاطف لنوع من الشبه بالمعطوف؛ لما بينهما من التغاير،",
     "en": "it remains only as it was in its being a qualifier, and the entry of the conjunctive particle is good only because of a kind of resemblance to the conjoined noun, owing to the difference between the two [qualifiers];"},
    {"type": "matn",
     "ar": "فلو حد المعطوف كذلك لدخل فيه بعض",
     "en": "so had the conjoined noun been defined thus, some…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يتجه عليه أن المراد بتوسط أحد الحروف العشرة توسط أحدها بتفصيل كما سيجيء، والواو التي لتأكيد اللصوق ليس من العشرة بالمعاني التي سيجيء.",
     "en": "The objection is directed against it that what is meant by the intervention of one of the ten particles is the intervention of one of them in the detailed sense that will come, and the wāw that serves to reinforce adherence is not among the ten in the meanings that will come."},
    {"type": "pair",
     "ar": "قلت: لا خلاف في جواز دخول «ثم» بين المؤكد والمؤكد، فينتقض التعريف به حينئذ.",
     "en": "I say: there is no disagreement over the permissibility of “thumma” entering between the corroborative and the corroborated, so the definition is then broken by it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة الشعراء: ٢٠٨.",
     "en": "Sūrat al-Shuʿarāʾ 26:208."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الفرق بين هذا الوجه والوجه الأول: أن الوجه الأول جعل المعطوف على الصفة صفة من وجه ومعطوفا من وجه،",
     "en": "The difference between this view and the first view: the first view makes the noun conjoined to the qualifier a qualifier in one respect and a conjoined noun in another,"},
    {"type": "pair",
     "ar": "وهذا الوجه جعله صفة لا محالة من غير أن يكون معطوفا من وجه.",
     "en": "while this view makes it a qualifier without exception, without its being a conjoined noun in any respect."},
]
