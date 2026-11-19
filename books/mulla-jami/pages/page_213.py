# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 213 (printed ٢١٢)."""

PAGE_NUMBER = 213
PRINTED_PAGE = "٢١٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(ولك) أي: وجاز لك (في مثل: «يا تيم تيم عدي») أي: في تركيب[[١]] تكرر فيه المنادى المفرد المعرفة صورة[[٢]] ولي الثاني اسم مجرور بالإضافة،",
     "en": "(And you may), that is, it is permitted to you, (in such as “yā Taymu Tayma ʿAdiyyin”—O Taym, Taym of ʿAdī), that is, in a construction in which a vocative that is in form singular and definite is repeated, and the second is followed by a noun in the genitive by annexation,"},
    {"type": "matn",
     "ar": "في الأول: (الضم والنصب)، وفي الثاني: النصب فحسب.",
     "en": "[use] in the first (the ḍamma and the accusative), and in the second the accusative only."},
    {"type": "matn",
     "ar": "أما الضم في الأول[[٣]]: فلأنه منادى مفرد معرفة كما هو الظاهر.",
     "en": "As for the ḍamma in the first: that is because it is a singular, definite vocative, as is evident."},
    {"type": "matn",
     "ar": "وأما النصب فعلى أنه مضاف إلى «عدي» المذكور، و«تيم» الثاني تأكيد لفظي[[٤]] فاصل بين المضاف والمضاف إليه، وذلك مذهب سيبويه[[٥]]",
     "en": "As for the accusative, it is on the basis that it is annexed to the “ʿAdī” that is mentioned, the second “Taym” being a verbal corroborative (taʾkīd lafẓī) separating the annexed noun from the noun annexed to it; that is the position of Sībawayh;"},
    {"type": "matn",
     "ar": "أو مضاف إلى «عدي»[[٦]] المحذوف بقرينة المذكور، وذلك مذهب المبرد،",
     "en": "or [it is] annexed to an elided “ʿAdī,” indicated by the one mentioned; that is the position of al-Mubarrad."},
    {"type": "matn",
     "ar": "والسيرافي أجاز الفتح[[٧]] مكان النصب على أن يكون في الأصل: «يا تيم -بالضم- تيم عدي» ففتح اتباعا لنصب الثاني كما في «يا زيد بن عمرو»،",
     "en": "Al-Sīrāfī allowed the fatḥa in place of the accusative, on the basis that the original is “yā Taymu—with the ḍamma—Tayma ʿAdiyyin,” and it was given the fatḥa in concord with the accusative of the second, as in “yā Zayda bna ʿAmrin.”"},
    {"type": "matn",
     "ar": "وتعين النصب في الثاني؛ لأنه إما تابع مضاف[[٨]] أو تابع مضاف[[٩]]، وتمام البيت:",
     "en": "The accusative is fixed in the second because it is either the appositive of an annexed noun or an annexed appositive. The full verse is:"},
    {"type": "verse",
     "ar": "يا تيم تيم عدي لا أبا لكم[[١٠]]          لا يلقينكم في سوءة عمر",
     "en": "O Taym, Taym of ʿAdī—you have no father!—let not ʿUmar cast you into disgrace."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أو فيما قصد ذكر المنادى مضافا، ثم كرر المضاف قبل ذكر المضاف إليه.",
     "en": "Or in that in which the vocative is meant to be mentioned annexed, and then the annexed noun is repeated before the noun annexed to it is mentioned."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أما أن الأول مفرد صورة فظاهر. وأما أن الثاني مفرد؛ فلأنه تكرار الأول بعينه.",
     "en": "That the first is singular in form is evident. That the second is singular is because it is the very repetition of the first."},
    {"type": "pair",
     "ar": "وأما عدي فحاله مجهولة بحسب الظاهر.",
     "en": "As for “ʿAdī,” its status is, on the face of it, unknown."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيل: نصب الثاني حينئذ ليس على أنه تأكيد؛ لأنه خرج عن العلمية بالإضافة،",
     "en": "It has been said: the accusative of the second is then not as a corroborative, because by annexation it has left the status of a proper name,"},
    {"type": "pair",
     "ar": "وأن القصد إلى المضاف يغاير القصد إلى المفرد، وأن المضاف أوضح من المفرد، فلا يكون عين الأول،",
     "en": "and because intending the annexed noun differs from intending the singular, and the annexed is clearer than the singular; so it is not identical with the first."},
    {"type": "pair",
     "ar": "فإذا كان الأول توطئة كان الثاني بدلا، وإذا كان مرادا كان الثاني عطف بيان.",
     "en": "If the first is a preparation, the second is a substitute; and if it is intended, the second is an explicative apposition."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وإنما جيء بتأكيد المضاف بينه وبين المضاف إليه لئلا يستنكر بقاء الثاني بلا مضاف إليه، ولا تنوين معوض عنه، ولا بناء على الضم،",
     "en": "The corroborative of the annexed noun was brought between it and the noun annexed to it only so that the second remaining without a noun annexed to it, without a tanwīn in compensation, and without being built on the ḍamma, should not be found objectionable."},
    {"type": "pair",
     "ar": "وجاز الفصل به بينهما في السعة؛ لأنه لما كرر الأول بلفظه وحركته بلا تغيير صار الثاني كأنه هو الأول، فكأنه لا فصل.",
     "en": "Separating the two by it was allowed in unconstrained speech because, the first being repeated in its wording and vowel without change, the second became as if it were the first, so it is as though there were no separation."},
    # REVIEW: print reads «إن «إن زيدا قائم»»; the intended example is unclear; transcribed as printed.
    {"type": "pair",
     "ar": "ألا ترى أنك تقول: إن «إن زيدا قائم» مع امتناع الفصل بين «إن» واسمها إلا بالظرف،",
     "en": "Do you not see that you say “inna inna Zaydan qāʾimun,” although separating “inna” from its noun is barred except by an adverbial (ẓarf),"},
    {"type": "pair",
     "ar": "وأنه قال: ولا لـ\"لما\" بهم أبدا دواء مع أن حرف الجر لا يدخل إلا على الاسم.",
     "en": "and that [the poet] said “wa-lā li-li-mā bihim abadan dawāʾu” (nor for what afflicts them is there ever a cure), although a preposition enters only on a noun?"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "المذهب لأستاده هو الخليل، وهو تابع له فيه.",
     "en": "The position belongs to his teacher, namely al-Khalīl, and he follows him in it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "المحذوف لئلا يلزم التقديم والتأخير والفصل.",
     "en": "[Annexed to] the elided [ʿAdī], so that neither anteposition and postposition nor separation is entailed."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "كان المصنف لم يختر، بل أشار إلى رده بتقديم الخبر، أعني: لك حتى ينحصر الاحتمال في الضم والنصب.",
     "en": "It is as if the author did not adopt it, but rather pointed to its rejection by putting the predicate first—I mean “laka” (you may)—so that the possibilities are confined to the ḍamma and the accusative."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "بالإضافة كما ذهب إليه سيبويه، وتأكيد لفظي، والتأكيد اللفظي في الأغلب حكمه حكم الأول، وحركته حركة إعرابية كانت أو بنائية،",
     "en": "[Annexed] by annexation, as Sībawayh held, and a verbal corroborative; and the verbal corroborative mostly has the rule of the first, and its vowel [is the first’s vowel], whether inflectional or indeclinable;"},
    {"type": "pair",
     "ar": "فكما أن الأول محذوف التنوين للإضافة كذلك الثاني مع أنه ليس بمضاف.",
     "en": "so just as the first has its tanwīn dropped because of annexation, so does the second, although it is not annexed."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "بالوصف كما هو مذهب المبرد والسيرافي.",
     "en": "[An appositive] by qualification, as is the position of al-Mubarrad and al-Sīrāfī."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "قال الجوهري في لا أبا لك: هو مدح، ومعناه: أنك ماجد شجاع لا تحتاج إلى من ينصرك ويقوم بأمرك.",
     "en": "Al-Jawharī said of “lā abā laka” (you have no father): it is praise, and its meaning is that you are noble and brave, needing no one to help you and see to your affairs."},
    {"type": "pair",
     "ar": "وقال الأزهري: هو شتم لا شتم فوقه، أي: لست بابن رشدة.",
     "en": "Al-Azharī said: it is an insult than which there is none greater, that is: you are not of legitimate birth (lasta bi-bni rishda)."},
]
