# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 567 (printed ٥٦٦)."""

PAGE_NUMBER = 567
PRINTED_PAGE = "٥٦٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "section", "ar": "[لكن]",
     "en": "Lākinna"},

    {"type": "matn",
     "ar": "(ولكن) وهي عند البصريين مفردة.",
     "en": "(And lākinna): according to the Baṣrans it is simple (mufrada)."},
    {"type": "matn",
     "ar": "وقال الكوفيون[[١]]: وهي مركبة من «لا وإن المكسورة المصدرة بالكاف الزائدة»، وأصله: «لا كإن»، فنقلت كسرة الهمزة إلى الكاف[[٢]]، وحذفت الهمزة،",
     "en": "The Kūfans said that it is compounded of “lā and inna with kasra, prefixed by a redundant kāf”, its origin being “lā ka-inna”; the kasra of the hamza was transferred to the kāf and the hamza was elided."},
    {"type": "matn",
     "ar": "فكلمة «لا» تفيد أن ما بعدها ليس كما قبلها، بل هو مخالف له نفيا وإثباتا، وكلمة «إن» تحقق مضمون ما بعدها.",
     "en": "So the word “lā” conveys that what follows it is not like what precedes it, but differs from it in negation and affirmation, while the word “inna” confirms the content of what follows it."},
    {"type": "matn",
     "ar": "(للاستدراك) ومعنى الاستدراك: رفع توهم يتولد من الكلام المتقدم.",
     "en": "(For rectification (istidrāk)). The meaning of rectification is removing a false impression that arises from the preceding speech."},
    {"type": "matn",
     "ar": "فإذا قلت: «جاءني زيد»، فكأنه توهم أن عمرا أيضا جاءك، لما بينهما من الألفة، فرفعت ذلك التوهم بقولك: «لكن عمرا لم يجئ».",
     "en": "So when you say “Zayd came to me”, it is as though it were imagined that ʿAmr also came to you, because of the familiarity between them; and you remove that impression by saying “but ʿAmr did not come”."},
    {"type": "matn",
     "ar": "(يتوسط) أي: «لكن» (بين كلامين متغايرين) نفيا وإثباتا (معنى) أي: تغايرا معنويا[[٣]].",
     "en": "(It stands in the middle), that is, “lākinna”, (between two utterances that differ) in negation and affirmation (in meaning), that is, with a difference in meaning."},
    {"type": "matn",
     "ar": "والضروري هو المعنوي، ولهذا اقتصر عليه.",
     "en": "What is necessary is [difference in] meaning; for this reason he confined himself to it."},
    {"type": "matn",
     "ar": "واللفظي قد يكون النفي صريحا نحو: «جاءني زيد لكن عمرا لم يجئ».",
     "en": "As for the verbal [difference], the negation is sometimes explicit, as in “Zayd came to me, but ʿAmr did not come”,"},
    {"type": "matn",
     "ar": "وقد لا يكون، نحو: «زيد حاضر لكن عمرا غائب».",
     "en": "and sometimes not, as in “Zayd is present, but ʿAmr is absent”."},
    {"type": "matn",
     "ar": "(وتخفف) أي: «لكن» (فتلغى) عن العمل؛ لخروجها عن المشابهة، وأشبهت العاطفة لفظا ومعنى، فأجريت مجراها،",
     "en": "(And it is lightened), that is, “lākinna”, (and then it is cancelled) from governing, because it has left [its] resemblance [to the verb] and has come to resemble the coordinating [lākin] in wording and meaning, so it was treated like it;"},
    {"type": "matn",
     "ar": "بخلاف «إن، وأن» المخففتين، فإنه ليس لهما ما أجريتا عليه.",
     "en": "unlike the lightened “in” and “an”, for there is nothing [of this kind] for them to be treated like."},
    {"type": "matn",
     "ar": "وفي بعض النسخ: «على الأكثر»، وكأنه إشارة إلى ما جاء عن يونس والأخفش من أنه يجوز إعمالها قياسا على أخواتها المخففة.",
     "en": "In some copies [there is the addition] “according to most usage”; it seems to allude to what is reported from Yūnus and al-Akhfash, that it may be made to govern by analogy with its lightened sisters."},
    {"type": "matn",
     "ar": "وقال الشارح الرضي: «ولا أعرف له شاهدا».",
     "en": "The commentator al-Raḍī said: “I know of no attestation (shāhid) for it.”"},
    {"type": "matn",
     "ar": "(ويجوز معها) مشددة ومخففة (الواو)، وهي إما لعطف الجملة على الجملة، وإما اعتراضية.",
     "en": "(And there may occur with it), whether doubled or lightened, (the wāw), which is either for coordinating clause with clause or parenthetical (iʿtirāḍiyya)."},
    {"type": "matn",
     "ar": "وجعل الشارح الرضي: الأخير أظهر.",
     "en": "The commentator al-Raḍī considered the latter the more evident."},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 566 (note ٣ there) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "خففت.",
     "en": "…it is lightened.”"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في الرضي: ولا يخفى أثر التكلف فيما قالوه، وفيه نقل الحركة إلى المتحرك، والأصل عدم التركيب، انتهى.",
     "en": "In al-Raḍī: “The trace of strained interpretation in what they said is not hidden; it involves transferring a vowel to a letter that is already voweled, and the default is the absence of compounding.” End of quotation."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال الرضي: فيه نقل الحركة إلى المتحرك.",
     "en": "Al-Raḍī said: this involves transferring a vowel to a letter that is already voweled."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يجب أن يكون عين الأول موهما لنقيض الثاني.",
     "en": "The first [utterance] must itself give the impression of the contradictory of the second."},
]
