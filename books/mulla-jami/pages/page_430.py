# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 430 (printed ٤٢٩)."""

PAGE_NUMBER = 430
PRINTED_PAGE = "٤٢٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «استثناء من قوله: «مجموع»؛» at the foot of PDF p. 429.
    {"type": "matn",
     "ar": "لأنهم لم يجمعوا «مائة» حين ميزوا بها ثلاثا وأخواتها (وكان قياسها[[١]]) أن يجمع فيقال: (مئات أو مئين)؛ لأن للمائة جمعين:",
     "en": "…because they did not put “miʾa” in the plural when they specified thalāth and its sisters with it. (Its regular form would have been) for it to be pluralized, so that one would say (miʾāt or miʾīn), because miʾa has two plurals:"},
    {"type": "matn",
     "ar": "أحدهما: في صورة جمع المذكر السالم[[٢]]، وهو «مئون».",
     "en": "the first in the form of the sound masculine plural, namely “miʾūn”;"},
    {"type": "matn",
     "ar": "والثاني: في صورة جمع المؤنث السالم، وهو مئات،",
     "en": "the second in the form of the sound feminine plural, namely miʾāt."},
    {"type": "matn",
     "ar": "ولا يجوز إضافة العدد إلى جمع المذكر السالم[[٣]]، فلا يقال: «ثلاثة مسلمين»، فلم يبق إلا «مئات»،",
     "en": "It is not permissible to annex a number to a sound masculine plural, so one does not say “thalāthat muslimīn”; so only “miʾāt” remained."},
    {"type": "matn",
     "ar": "لكنهم كرهوا أن يلي التمييز المجموع[[٤]] بالألف والتاء بعد ما تعود[[٥]] المجيء بعدما هو في صورة المجموع بالواو والنون، أعني: «عشرين إلى تسعين»،",
     "en": "But they disliked that the specifier should follow what is pluralized with alif and tāʾ, after it had become accustomed to coming after what is in the form of the plural with wāw and nūn, I mean “ʿishrīn to tisʿīn”;"},
    {"type": "matn",
     "ar": "فاقتصر على المفرد مع كونه أخصر.",
     "en": "so the singular was kept to, besides its being more concise."},
    {"type": "matn",
     "ar": "(ومميز «أحد عشر» إلى «تسعة وتسعين») بل إلى تسع وتسعين (منصوب مفرد)",
     "en": "(The specifier of “aḥada ʿashara” [eleven] to “tisʿa wa-tisʿīn” [ninety-nine]), or rather to tisʿ wa-tisʿīn, (is accusative and singular)."},
    {"type": "matn",
     "ar": "أما نصبه في العقود، فلتعذر الإضافة[[٦]]؛ إذ لا يستقيم إبقاء النون معها؛ إذ هي في صورة نون الجمع، ولا حذفها؛ إذ ليست هي في الحقيقة نون الجمع.",
     "en": "As for its being accusative in the decades, it is because annexation is impossible: the nūn cannot properly be kept with it, since it has the form of the plural nūn; nor can it be dropped, since it is not in reality the plural nūn."},
    {"type": "matn",
     "ar": "وأما في ما عداها، فلأنهم كرهوا أن يصيروا ثلاثة أسماء كالاسم الواحد،",
     "en": "As for what is other than them, it is because they disliked that three nouns should become like a single noun."},
    {"type": "matn",
     "ar": "ولا يرد عليه «خمسة عشرك»؛ لأن المضاف إليه فيه لما كان غير مميز العدد لم يمتزج امتزاج ذلك المميز، فلم يلزم صيرورة ثلاثة أشياء شيئا واحدا،",
     "en": "“Khamsata ʿasharaka” (your fifteen) does not count against this, because the annexed term in it, not being the specifier of the number, does not fuse as that specifier would; so it does not follow that three things become one thing."},
    # REVIEW: «ثلثمائة» is printed (older spelling without alif); transcribed as printed.
    {"type": "matn",
     "ar": "وإنما جوزوا «ثلثمائة امرأة» مع أن فيها صيرورة ثلاثة أشياء شيئا واحدا ليطرد بـ«مائة امرأة»،",
     "en": "They allowed “thalāthumiʾat imraʾa” (three hundred women), although three things become one thing in it, only so that it would run parallel to “miʾat imraʾa” (a hundred women)."},
    {"type": "matn",
     "ar": "وأما إفراده، فلأنه لما صار منصوبا صار فضلة، فاعتبر إفراده ليكون الفضلة قليلا.",
     "en": "As for its being singular, it is because, having become accusative, it became a complement (faḍla), so its singularity was taken into account so that the complement would be small."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: بالنظر إلى كون مميزها مجموعا، فلا ينافي عدم مجيء إضافة العدد إلى جمع المذكر السالم.",
     "en": "That is, in view of its specifier’s being plural; so it does not conflict with the non-occurrence of annexing a number to a sound masculine plural."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إنما قال: في صورة جمع المذكر السالم، ولم يقل: في صورة جمع المؤنث السالم؛ لأنه اختلف في مئين،",
     "en": "He said “in the form of the sound masculine plural” and did not say [likewise] “in the form of the sound feminine plural” only because there is disagreement about miʾīn."},
    {"type": "pair",
     "ar": "قال الأخفش: هو فعلين كغسلين، فهو عنده اسم الجمع.",
     "en": "Al-Akhfash said: it is of the pattern fiʿlīn, like ghislīn; so for him it is a collective noun (ism al-jamʿ)."},
    {"type": "pair",
     "ar": "وقال بعضهم: هو فعيل كعصى أبدل الياء الأخير نونا.",
     "en": "Others said: it is of the pattern fuʿīl, like ʿuṣiyy, with the final yāʾ replaced by a nūn."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قد نبه بذلك على أن قول المصنف وكان قياسها مئات أو مئين غير مستقيم، والقياس مئات لا غير.",
     "en": "By this he has indicated that the author’s words “its regular form would have been miʾāt or miʾīn” are not sound; the regular form is miʾāt and nothing else."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: أن يلي التمييز الذي يذكر للمائة كما يقال: مائة رجل، كذا نقل عن الشارح الرضي.",
     "en": "That is, that the specifier mentioned for miʾa, as one says “miʾat rajul” (a hundred men), should follow [it]; so it is reported from the commentator al-Raḍī."},
    {"type": "pair",
     "ar": "فالتمييز فاعل «يلي»، والمجموع مفعول له.",
     "en": "So “the specifier” is the agent of “yalī” (follow), and “what is pluralized” is its object."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: أخذ التمييز المجيء بعد ما هو في صورة الجمع إلى آخره عادة،",
     "en": "That is, after the specifier had taken as habit coming after what is in the form of the plural, and so on;"},
    {"type": "pair",
     "ar": "فالضمير المستتر في «تعود» راجع إلى التمييز، والمجيء مفعوله.",
     "en": "so the concealed pronoun in “taʿawwada” (became accustomed) refers to the specifier, and “coming” is its object."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: «من يضيف عشرون «من» وأخواتها» is printed as such (nominative «عشرون» and a quoted «من»); transcribed as printed.
    {"type": "pair",
     "ar": "حكى الكسائي أن من العرب من يضيف عشرون «من» وأخواتها إلى المميز منكورا، نحو: عشرون درهم، ومعرفا نحو: عشرون ثوبه،",
     "en": "Al-Kisāʾī reported that some Arabs annex ʿishrūn and its sisters to the specifier, indefinite, as in “ʿishrū dirhamin” (twenty dirhams), and definite, as in “ʿishrū thawbihi” (twenty of his garments);"},
    {"type": "pair",
     "ar": "وعند الأكثرين هو شاذ لا يبنى على مثله قاعدة، كذا في شرح التسهيل للفاضل المصري.",
     "en": "but according to most it is anomalous, and no rule is built on the like of it. So it is in Sharḥ al-Tashīl by al-Fāḍil al-Miṣrī."},
]
