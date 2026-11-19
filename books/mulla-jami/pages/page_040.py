# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 40 (printed ٣٩)."""

PAGE_NUMBER = 40
PRINTED_PAGE = "٣٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "قبل الوضع، وليس الأمر كذلك، فإن اتصاف المعنى بالإفراد والتركيب إنما هو بعد الوضع،",
     "en": "before the positing (waḍʿ); but the matter is not so, for the meaning’s being qualified by singularity (ifrād) and composition (tarkīb) occurs only after the positing,"},
    {"type": "matn",
     "ar": "فينبغي أن لا يرتكب فيه[[١]] تجوز، كما يرتكب في مثل: «من قتل قتيلا»[[٢]].",
     "en": "so no figurative usage (tajawwuz) should be committed regarding it, as is committed in the like of “whoever kills a slain one” [i.e., one who is about to be slain]."},

    {"type": "matn",
     "ar": "٢- أو مرفوع على أنه صفة لـ«لفظ»، ومعناه[[٣]] حينئذ: ما لا يدل جزؤه[[٤]] على جزء معناه.",
     "en": "2— Or it is nominative (marfūʿ), on the basis that it is an adjective qualifying “lafẓ” (word); and its sense in that case is: that whose part does not signify a part of its meaning."},
    {"type": "matn",
     "ar": "ولا بد حينئذ من بيان نكتة[[٥]] في إيراد أحد الوصفين جملة فعلية، والآخر[[٦]] مفردا.",
     "en": "In that case there must be an account of a subtle point (nukta) in presenting one of the two attributes as a verbal sentence (jumla fiʿliyya) and the other as a single term (mufrad)."},
    {"type": "matn",
     "ar": "وكأن[[٧]] النكتة فيه التنبيه على تقدم الوضع على الإفراد، حيث أتى به بصيغة المضي[[٨]]، بخلاف الإفراد.",
     "en": "It is as if the subtle point in it is to alert one to the precedence of the positing (waḍʿ) over singularity, since he expressed it with the past-tense form (waḍaʿa), unlike singularity."},

    {"type": "matn",
     "ar": "٣- وأما نصبه وإن لم يساعده رسم الخط، فعلى أنه حال من الضمير المستكن في «وضع»[[٩]]،",
     "en": "3— As for reading it in the accusative (naṣb) — even though the written form does not support it — it is on the basis that it is a circumstantial qualifier (ḥāl) of the concealed pronoun in “waḍaʿa,”"},
    {"type": "matn",
     "ar": "أو من «المعنى»[[١٠]]، فإنه[[١١]] مفعول به[[١٢]] بواسطة اللام.",
     "en": "or of “the meaning” (al-maʿnā), for it is the object (mafʿūl bihi) by means of the lām."},
    {"type": "matn",
     "ar": "ووجه صحته[[١٣]]: أن الوضع وإن كان متقدما على الإفراد بحسب الذات، لكنه مقارن له بحسب الزمان، وهذا القدر كاف لصحة الحالية[[١٤]].",
     "en": "The aspect of its correctness is: that the positing, although prior to singularity in essence (bi-ḥasab al-dhāt), is concurrent with it in time; and this much suffices for the validity of the circumstantial construction (ḥāliyya)."},

    {"type": "rule"},

    # continuation of the last footnote from the previous page
    {"type": "note", "num": "…"},
    {"type": "pair",
     "ar": "بسببه. وإنما قال: «يوهم» مع أن القاعدة تقتضيه اقتضاء بينا لظهور المراد ههنا.",
     "en": "…by reason of it. He said only “it gives the impression” (yūhim), even though the rule requires it in a manifest manner, because the intended sense is evident here."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: في دفع الإيهام.",
     "en": "That is: in warding off the ambiguity (īhām)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وهو مجاز بطريق المشارفة، فكذا في المفرد.",
     "en": "This is a figurative usage by way of imminence (mushārafa) [naming a thing by what it is about to become]; and so too in [the case of] “al-mufrad.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: معنى اللفظ المفرد.",
     "en": "That is: the meaning of the single word."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "من حيث إنه لا يدل على جزء معناه. المفهوم من كلام الشيخ الرضي: أن الإفراد صفة اللفظ عند المنطقيين، وصفة للمعنى عند النحاة،",
     "en": "In respect of its not signifying a part of its meaning. What is understood from the words of Shaykh al-Raḍī is: that singularity (ifrād) is an attribute of the word (lafẓ) according to the logicians, and an attribute of the meaning according to the grammarians;"},
    {"type": "pair",
     "ar": "لكن المشهور أن الإفراد في عرف النحاة صفة للفظ بالذات، وبالعرض للمعنى.",
     "en": "yet the well-known view is that singularity, in the convention of the grammarians, is an attribute of the word essentially (bi-l-dhāt) and of the meaning accidentally (bi-l-ʿaraḍ)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لأن المتكلم بليغ لا يظن به أن يخلو اختياره هذه الخصوصية عن نكتة.",
     "en": "Because the speaker is eloquent (balīgh); it is not supposed of him that his choosing this particular feature would be devoid of a subtle point (nukta)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا يخفى لطف هذا البيان.",
     "en": "The subtlety of this explanation is not hidden."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أتى بـ«كأن» الدال على الشك والظن إشارة إلى أنه يمكن أن يكون النكتة غيرها.",
     "en": "He used “ka-anna” (as if), which denotes doubt and conjecture, to indicate that the subtle point could possibly be something other than this."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "فاستعيرت صيغة السبق الزماني للسبق الرتبي.",
     "en": "So the form denoting temporal precedence was borrowed [metaphorically] for rank-precedence (al-sabq al-rutbī)."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "إن قلت: لو كان حالا منه لكان يجنبه كما في: «ضربت قائما زيدا»؟",
     "en": "If you say: were it a ḥāl of it, it would be set alongside it [freely positioned], as in “ḍarabtu qāʾiman Zaydan” (I struck Zayd standing)?"},
    {"type": "pair",
     "ar": "قلنا: لا نسلم لزوم ذلك عند الكل، فإن بعضهم يراعون رتبة الحال، وهي التأخير عن الفاعل والمفعول به.",
     "en": "We say: we do not concede that this is obligatory in the view of all, for some observe the [proper] rank of the ḥāl, namely its coming after the subject (fāʿil) and the object (mafʿūl bihi)."},
    {"type": "pair",
     "ar": "ولئن سلم فذلك إذا لم تكن قرينة دالة على تعيين ذي الحال، وقد تحققت ههنا؛ لأن الإفراد صفة للفظ بالذات، أو إذا تغير المعنى على تقدير جعله حالا عما يليه.",
     "en": "And even if it be conceded, that [preposing is barred] only when there is no indication (qarīna) specifying the possessor of the state (dhū al-ḥāl) — yet such an indication is realized here, because singularity is an attribute of the word essentially — or when the meaning would change on the supposition of making it a ḥāl of what is adjacent to it."},
    {"type": "pair",
     "ar": "ولا خفاء في أن إفراد المعنى يؤول إلى إفراد اللفظ.",
     "en": "And there is no obscurity in that the singularity of the meaning ultimately resolves into the singularity of the word."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "ولم يتقدم عليه مع أنه نكرة؛ لأنه لا يتقدم الحال على ذي الحال المجرور.",
     "en": "It [the ḥāl] was not preposed before it, even though it [the possessor of the state] is indefinite (nakira), because the ḥāl is not preposed before a possessor of the state that is in the genitive (majrūr)."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "أي: المعنى.",
     "en": "That is: the meaning."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "للفعل. واللام واسطة في كونه مفعولا ومعمولا به، فاتحد عامل الحال وصاحبها.",
     "en": "Of the verb. The lām is the intermediary in its being an object and a governed element, so the governing agent (ʿāmil) of the ḥāl and its possessor are one and the same."},

    # ---------------- Footnote 13 ----------------
    {"type": "note", "num": "١٣"},
    {"type": "pair",
     "ar": "أي: وجه صحة وقوع المفرد حالا سواء كان من الضمير المستكن في «وضع» أو من «المعنى».",
     "en": "That is: the aspect of the validity of the single word’s occurring as a ḥāl, whether it be [a ḥāl] of the concealed pronoun in “waḍaʿa” or of “the meaning.”"},

    # ---------------- Footnote 14 ----------------
    {"type": "note", "num": "١٤"},
    {"type": "pair",
     "ar": "لا دخل للمعية الذاتية في الحالية. ولا يتفاوت بها الحال كما يوهمه قوله: وهذا القدر كاف لصحة الحالية.",
     "en": "Essential concomitance (al-maʿiyya al-dhātiyya) has no bearing on the circumstantial construction (ḥāliyya), nor does the ḥāl vary on account of it, contrary to what his statement might suggest: “and this much suffices for the validity of the circumstantial construction.”"},
]
