# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 277 (printed ٢٧٦)."""

PAGE_NUMBER = 277
PRINTED_PAGE = "٢٧٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the discussion of the verse «أتهجر سلمى بالفراق حبيبها…» from the foot of PDF p. 276.
    {"type": "matn",
     "ar": "على تقدير تأنيث الضمير في «تطيب»، فإنه حينئذ يكون في «كاد» ضمير الشأن لتذكيره، ويعود ضمير «تطيب» إلى «سلمى»، ويكون «نفسا» تمييزا عن نسبة «تطيب» إليها مقدما عليه،",
     "en": "…on the assumption that the pronoun in “taṭību” is feminine; for then there is in “kāda” the pronoun of the matter (ḍamīr al-shaʾn), since it is masculine, the pronoun of “taṭību” refers to “Salmā,” and “nafsan” is a specification of the relation of “taṭību” to her, placed before it."},
    {"type": "matn",
     "ar": "وأما على تقدير تذكير الضمير، فضمير «كاد» للحبيب، و«نفسا» تمييز عن نسبة «كاد» إليه، أي: وما كاد الحبيب نفسا يطيب فلا تمسك،",
     "en": "But on the assumption that the pronoun is masculine, the pronoun of “kāda” is for the beloved, and “nafsan” is a specification of the relation of “kāda” to him, that is: “and the beloved was scarcely, in soul, content”; so there is no support [in the verse]."},
    {"type": "matn",
     "ar": "وما قيل[[١]]: يحتمل أن يحمل البيت على تقدير تأنيثه أيضا على هذا الوجه بأن يكون تأنيث الضمير الراجع إلى الحبيب باعتبار النفس؛",
     "en": "As for what has been said—that the verse may also be taken on the assumption of the feminine in this way, the pronoun referring to the beloved being feminine in view of “soul”—"},
    {"type": "matn",
     "ar": "إذ المعنى: «وما كادت نفس الحبيب تطيب» فتكلف وتعسف غير قادح في التمسك[[٢]].",
     "en": "since the meaning is “and the soul of the beloved was scarcely content”: that is strained and forced, and does not impair the [use of the verse as] support."},

    {"type": "section", "ar": "[الاستثناء]",
     "en": "The Exception (al-Istithnāʾ)"},

    {"type": "matn",
     "ar": "(المستثنى) أي: ما يطلق عليه لفظ المستثنى في اصطلاح النحاة على قسمين،",
     "en": "(The excepted term, al-mustathnā)—that is, what the word mustathnā is applied to in the technical usage of the grammarians—is of two kinds."},
    {"type": "matn",
     "ar": "ولما كان معلوميته بهذا الوجه الغير المحتاج إلى التعريف كافية في تقسيمه قسمه إلى قسمين، وعرف كل واحد منهما؛",
     "en": "Since its being known in this way, which needs no definition, sufficed for dividing it, he divided it into two kinds and defined each of them;"},
    {"type": "matn",
     "ar": "لأن لكل واحد منهما أحكاما خاصة لا يمكن إجزاؤها عليه إلا بعد معرفته، فقال: (متصل، ومنقطع).",
     "en": "because each of them has particular rules that cannot be applied to it except after it is known. So he said: (connected, muttaṣil, and disconnected, munqaṭiʿ)."},
    {"type": "matn",
     "ar": "(فالمتصل: هو المخرج) أي: الاسم الذي أخرج، واحترز به عن غير المخرج كجزئيات المستثنى المنقطع",
     "en": "(The connected is what is taken out), that is, the noun that has been taken out; by this he excluded what is not taken out, such as the particular instances of the disconnected excepted term,"},
    {"type": "matn",
     "ar": "(عن متعدد) أي: جزئياته نحو: «ما جاءني أحد إلا زيدا»، أو أجزائه مثل: «اشتريت العبد إلا نصفه»",
     "en": "(from a plurality), that is, from its particulars, as in “No one came to me except Zayd,” or from its parts, as in “I bought the slave except half of him,”"},
    {"type": "matn",
     "ar": "سواء كان ذلك المتعدد (لفظا) أي: ملفوظا نحو: «جاءني القوم إلا زيدا» (أو تقديرا) أي: مقدرا، نحو: «ما جاءني إلا زيد» أي: «ما جاءني أحد إلا زيدا»",
     "en": "whether that plurality is (in wording), that is, uttered, as in “The people came to me except Zayd,” (or by implication), that is, implied, as in “None came to me but Zayd,” that is, “No one came to me except Zayd,”"},
    {"type": "matn",
     "ar": "(بـ«إلا») غير الصفة (وأخواتها). واحترز به عن نحو: «جاءني القوم إلا زيد»، و«ما جاءني القوم لكن زيد جاء».",
     "en": "(by “illā”)—not the adjectival [illā]—(and its sisters). By this he excluded such cases as “The people other than Zayd came to me” and “The people did not come to me, but Zayd came.”"},
    {"type": "matn",
     "ar": "(و) المستثنى (المنقطع: هو المذكور بعدها) أي: بعد «إلا» وأخواتها[[٣]] (غير مخرج عن متعدد).",
     "en": "(And) the (disconnected) excepted term (is what is mentioned after them), that is, after “illā” and its sisters, (not taken out from a plurality)."},
    {"type": "matn",
     "ar": "واحترز به عن جزئيات المستثنى المتصل، فالمستثنى الذي لم يكن داخلا في المتعدد قبل الاستثناء منقطع،",
     "en": "By this he excluded the particular instances of the connected excepted term. So the excepted term that was not included in the plurality before the exception is disconnected,"},
    {"type": "matn",
     "ar": "سواء كان من جنسه كقولك: «جاءني القوم إلا زيدا» مشيرا بالقوم إلى جماعة خالية عن «زيد»، أو لم يكن نحو: «جاءني القوم إلا حمارا».",
     "en": "whether it is of its genus, as when you say “The people came to me except Zayd,” referring by “the people” to a group not including Zayd, or not, as in “The people came to me except a donkey.”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قيل: يحتمل أيضا أن يكون تطيب المذكور مفسرا لتطيب المقدر قبل نفسا.",
     "en": "It has been said: it is also possible that the “taṭību” mentioned explains a “taṭību” implied before “nafsan.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إذ بناء تمسكهم على الظاهر الذي يقبله الطبع السليم.",
     "en": "For their use of it as support is built on the apparent sense, which sound taste accepts."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا يكون المنقطع إلا بعد إلا وغير وبيد مضافا إلى أن مشددة.",
     "en": "The disconnected [excepted term] occurs only after “illā,” “ghayr,” and “bayda” annexed to “anna” with doubled nūn."},
]
