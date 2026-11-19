# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 382 (printed ٣٨١)."""

PAGE_NUMBER = 382
PRINTED_PAGE = "٣٨١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «"اللوا" بحذف التاء والياء معا.» at the foot of PDF p. 381 (new sentence).
    {"type": "matn",
     "ar": "(وما) بمعنى: الذي فيما لا يعقل غالبا نحو: «عرفت ما عرفته»، وجاء فيما يعقل نحو: ﴿والسماء وما بناها﴾[[١]]",
     "en": "(Mā), meaning alladhī, mostly for what lacks reason, as in “ʿaraftu mā ʿaraftahu” (I knew what you knew); it also occurs for what has reason, as in “By the heaven and That which built it”;"},
    {"type": "matn",
     "ar": "(ومن) أيضا بمعناه فيمن يعقل، ويستوي فيهما المفرد والمثنى والمجموع، والمذكر والمؤنث",
     "en": "(man), also with its meaning, for those who have reason; in both, singular, dual and plural, masculine and feminine are alike;"},
    {"type": "matn",
     "ar": "(وأي[[٢]]) بمعنى «الذي»[[٣]]، نحو: «اضرب أيهم في الدار» أي: اضرب الذي في الدار",
     "en": "(ayy), meaning “alladhī”, as in “iḍrib ayyahum fī al-dār” (strike whichever of them is in the house), that is, strike the one who is in the house;"},
    {"type": "matn",
     "ar": "(وأية) بمعنى: «التي»، نحو: «اضرب أيتهن في الدار» أي: اضرب التي في الدار",
     "en": "(ayyatu), meaning “allatī”, as in “iḍrib ayyatahunna fī al-dār”, that is, strike the one [fem.] who is in the house;"},
    {"type": "matn",
     "ar": "(و«ذو» الطائية) أي: المنسوبة إلى بني طي لاختصاص مجيئها موصولة بلغتهم بمعنى «الذي أو التي»، قال الشاعر:",
     "en": "(and the Ṭāʾī “dhū”), that is, the one ascribed to the Banū Ṭayy, since its occurrence as a relative noun meaning “alladhī or allatī” is peculiar to their dialect. The poet said:"},
    {"type": "verse",
     "ar": "..................          وبئري ذو حفرت وذو طويت",
     "en": "…  and my well, the one I dug and the one I lined with stone,"},
    {"type": "matn",
     "ar": "أي: التي حفرتها والتي طويتها",
     "en": "that is, the one I dug and the one I lined;"},
    {"type": "matn",
     "ar": "(و«ذا» بعد «ما»[[٤]]) الكائنة (للاستفهام) نحو: «ماذا صنعت؟» أي: ما الذي صنعت",
     "en": "(and “dhā” after “mā”) when that is (interrogative), as in “mādhā ṣanaʿta?” (what did you do?), that is, what is it that you did;"},
    {"type": "matn",
     "ar": "(والألف واللام) أي: مجموعهما بمعنى: الذي أو التي، أو المثنى، أو المجموع.",
     "en": "(and alif-lām), that is, the two together, meaning alladhī or allatī, or the dual, or the plural."},
    {"type": "matn",
     "ar": "(والعائد المفعول[[٥]]) أي: العائد الذي لا يتم الموصول إلا به إذا كان مفعولا (يجوز حذفه) إذا لم يمنع مانع؛ لأنه فضلة،",
     "en": "(The returning pronoun that is an object), that is, the returning pronoun without which the relative noun is not complete, when it is an object, (may be elided) if nothing prevents it, because it is a complement (faḍla);"},
    {"type": "matn",
     "ar": "لا إذا كان فاعلا؛ لكونه عمدة، نحو قوله تعالى: ﴿الله يبسط الرزق لمن يشاء ويقدر له﴾[[٦]] أي: لمن يشاءه.",
     "en": "not when it is an agent, because that is a pillar (ʿumda); as in His words, the Exalted, “Allah extends provision to whom He wills and restricts it for him”, that is, to whom He wills it."},
    {"type": "matn",
     "ar": "واعلم أن النحاة وضعوا بابا يسمونه «باب الإخبار بالذي أو ما يقوم مقامه»،",
     "en": "Know that the grammarians laid down a chapter they call “the chapter on making a predication with alladhī or what stands in its place”;"},
    {"type": "matn",
     "ar": "ومقصودهم من وضعه تمرين المتعلم[[٧]] فيما تعلمه في هذا الفن من المسائل وتذكيره إياها[[٨]]،",
     "en": "their aim in laying it down is to exercise the learner in the questions of this discipline he has learned and to remind him of them;"},
    {"type": "matn",
     "ar": "فإنهم إذا قالوا لأحد: أخبر عن الاسم الفلاني في الجملة الفلانية بـ«الذي»",
     "en": "for when they say to someone, “make a predication about such-and-such a noun in such-and-such a sentence with ‘alladhī’” …"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الشمس: ٥.",
     "en": "Qurʾān, Sūrat al-Shams 91:5."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "مضافا إلى معرفة ظاهرة كانت أو مقدرة.",
     "en": "Annexed to a definite noun, whether overt or implied."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وفرعيه، وكذا في قوله: بمعنى التي.",
     "en": "And its two derived forms; likewise in his words “meaning allatī”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "جوز الكوفيون كون «ذا»، وجميع أسماء الإشارة موصولة بعد «ما» استفهامية كانت أو لا،",
     "en": "The Kūfans allowed “dhā”, and all the demonstratives, to be relative nouns after “mā”, whether interrogative or not;"},
    # REVIEW: «زائدة «إذ» بعده موصول» printed with «إذ» in guillemets; the sense is «زائدة؛ إذ بعده موصول». Transcribed as printed.
    {"type": "pair",
     "ar": "ولم يجوز البصريون ذلك إلا في «ذا» بشرط كونه بعد «ما» استفهامية إذا لم تكن زائدا، كما في قوله تعالى: ﴿من ذا الذي يقرض الله قرضا حسنا﴾ (البقرة: ٢٤٥، الحديد: ١١)، من ذا الذي أي: من الذي، فإن «ذا» زائدة «إذ» بعده موصول.",
     "en": "the Baṣrans allowed it only for “dhā”, on condition that it come after interrogative “mā”, when it is not redundant, as in His words, the Exalted, “Who is it that will lend Allah a goodly loan?” (Qurʾān, Sūrat al-Baqara 2:245; Sūrat al-Ḥadīd 57:11): “man dhā alladhī”, that is, “man alladhī”, for “dhā” is redundant, since a relative noun comes after it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سوى عائد الألف واللام، فإنه لا يجوز حذفه لخفاء موصوليتها، والضمير أحد دلائل موصوليتها.",
     "en": "Except the returning pronoun of alif-lām, which may not be elided because its relative status is hidden, and the pronoun is one of the indications of its relative status."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: Sūrat al-ʿAnkabūt 29:62 reads «لمن يشاء من عباده ويقدر له»; the matn quotes it without «من عباده». Transcribed as printed.
    {"type": "pair",
     "ar": "سورة العنكبوت: ٦٢.",
     "en": "Qurʾān, Sūrat al-ʿAnkabūt 29:62."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: تجربته. التمرين التمكين والتدريب.",
     "en": "That is, testing him. Tamrīn is establishing [in skill] and training."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "كما يتذكر مثلا بمعرفة أن الحال والتمييز لا يخبر عنهما أنه يجب تنكيرهما،",
     "en": "As, for example, by knowing that the circumstantial qualifier (ḥāl) and the specification (tamyīz) cannot be predicated about, he is reminded that they must be indefinite;"},
    {"type": "pair",
     "ar": "وبمعرفة أن المجرور بـ«حتى» وكاف التشبيه لا يخبر عنهما؛ لأنهما لا يقعان مضمرين.",
     "en": "and by knowing that what is governed in the genitive by “ḥattā” and by the kāf of comparison cannot be predicated about, [he is reminded] that these two do not occur with a pronoun."},
]
