# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 373 (printed ٣٧٢)."""

PAGE_NUMBER = 373
PRINTED_PAGE = "٣٧٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فعلى هذا لو لم» at the foot of PDF p. 372.
    {"type": "matn",
     "ar": "يحمل التقديم على ما ذكرنا انتقض القاعدة بقولنا: «الشأن هو زيد قائم»[[١]] على أن يكون «هو» مبتدأ راجعا إلى الشأن، و«زيد قائم» خبرا عنه،",
     "en": "…precedence is taken as we have stated, the rule is broken by our saying “al-shaʾnu huwa Zaydun qāʾimun” (the matter: it is that Zayd is standing), on the view that “huwa” is a subject referring back to “al-shaʾn” and “Zaydun qāʾimun” its predicate;"},
    {"type": "matn",
     "ar": "فإنه يصدق عليه أنه ضمير غائب، تقدم الجملة، مفسر بالجملة بعده،",
     "en": "for it is true of it that it is a third-person pronoun, that it precedes the sentence, and that it is explained by the sentence after it,"},
    {"type": "matn",
     "ar": "فإنه باعتبار رجوعه إلى الشأن لا يخرج عن الإبهام بالكلية، بل إنما يرتفع بجملة «زيد قائم»، كما لا يخفى.",
     "en": "since, by virtue of its referring back to “al-shaʾn”, it does not wholly leave vagueness; rather, the vagueness is removed only by the sentence “Zaydun qāʾimun”, as is not hidden."},
    {"type": "matn",
     "ar": "(ويكون) ضمير الشأن أو القصة (متصلا ومنفصلا) وإذا كان متصلا يكون (مستترا وبارزا[[٢]] على حسب العوامل)",
     "en": "(It is) — the pronoun of the matter or of the story — (attached and detached); and when it is attached it is (latent and overt, according to the governors)."},
    {"type": "matn",
     "ar": "فإن كان عامله معنويا[[٣]] بأن كان مبتدأ[[٤]] كان منفصلا، وإن كان لفظيا يصلح لاستتار الضمير فيه كان مستترا، وإلا بارزا",
     "en": "If its governor is abstract (maʿnawī), in that it is a subject, it is detached; if [its governor] is verbal (lafẓī) and suited to the pronoun’s being latent in it, it is latent; otherwise it is overt,"},
    {"type": "matn",
     "ar": "(مثل: «هو زيد قائم») مثال للمنفصل.",
     "en": "(as in “huwa Zaydun qāʾimun”) (it is [that] Zayd is standing): an example of the detached."},
    {"type": "matn",
     "ar": "(و«كان زيد قائم») مثال للمتصل المستتر.",
     "en": "(and “kāna Zaydun qāʾimun”) (it was [that] Zayd is standing): an example of the latent attached."},
    {"type": "matn",
     "ar": "(و«إنه زيد قائم») مثال للمتصل البارز.",
     "en": "(and “innahu Zaydun qāʾimun”) (indeed it is [that] Zayd is standing): an example of the overt attached."},
    {"type": "matn",
     "ar": "(وحذفه) عن اللفظ بإضماره لا نسيا منسيا حال كونه (منصوبا ضعيف) أي: جائز مع ضعف،",
     "en": "(Its omission) from the utterance — by its being understood, not by its being utterly forgotten — when it is (accusative, is weak), that is, permitted, but weak;"},
    {"type": "matn",
     "ar": "بخلاف ما إذا كان مرفوعا، فإنه لا يجوز أصلا، لكونه عمدة[[٥]].",
     "en": "unlike when it is nominative, for then it is not permitted at all, since it is a principal element (ʿumda)."},
    {"type": "matn",
     "ar": "أما جوازه، فلكونه على صورة الفضلات. وأما ضعفه، فلأنه حذف ضمير مراد بلا دليل عليه؛ لأن الخبر كلام مستقل،",
     "en": "As for its being permitted, that is because it has the form of the complements (faḍalāt). As for its weakness, that is because it is the omission of an intended pronoun without any indication of it, since the predicate is an independent statement."},
    {"type": "matn",
     "ar": "مثاله[[٦]]:",
     "en": "An example of it:"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 372 (note ٧ there) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "لا تفسيرا للمضمر وإثبات أنه لم يرجع إلى الشأن المتعين في المقام، وذكر على الإبهام، ففسر دونه خرط القتاد.",
     "en": "…not an explanation of the pronoun; and to establish that it does not refer to the matter that is determinate in the context, but was mentioned in vagueness and then explained, is harder than stripping the tragacanth (kharṭ al-qatād)."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: «لانتفضت» printed (with fāʾ); the context («الانتقاض», «انتقاض القاعدة») calls for «لانتقضت»; transcribed as printed.
    {"type": "pair",
     "ar": "لما رأى أن التوجيه السابق بقوله: يتقدم بعيد أيده بتوقف إتمام القاعدة عليه؛ إذ لولاه لانتفضت بهذا القول.",
     "en": "When he saw that the earlier interpretation of his word “yataqaddamu” (it precedes) was far-fetched, he supported it by [showing] that completing the rule depends on it, since without it the rule would be broken by this statement."},
    {"type": "pair",
     "ar": "ووجه الانتقاض: أنه لا يجب تفسير هذا الضمير بالجملة، بل يصح بالمفرد بأن يقال: الشأن هو قيام زيد.",
     "en": "The respect in which it is broken: this pronoun need not be explained by a sentence; it may properly be [explained] by a single word, as by saying “al-shaʾnu huwa qiyāmu Zaydin” (the matter: it is Zayd’s standing)."},
    {"type": "pair",
     "ar": "ولا يخفى عليك أن هذا التركيب مصنوع مستغنى عنه بمجرد هو زيد قائم، فلا مبالاة بانتقاض القاعدة به.",
     "en": "It will not be hidden from you that this construction is contrived, and can be dispensed with by the bare “huwa Zaydun qāʾimun”; so there is no concern about the rule’s being broken by it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فالأولى عدم الفصل بين هذا التفصيل والمتصل بالمنفصل.",
     "en": "So it would have been better not to separate this subdivision from “attached” by [the word] “detached”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لم يأت بحق التفصيل. وحقه أن يقال: إن كان معنويا أو حرفا، وهو مرفوعا كان منفصلا،",
     "en": "He did not give the subdivision its due. Its due is to say: if [the governor] is abstract, or a particle while it [the pronoun] is nominative, it is detached;"},
    {"type": "pair",
     "ar": "وإلا فإن كان مرفوعا يكون مستترا، وإلا فبارزا.",
     "en": "otherwise, if it is nominative it is latent, and if not, overt."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أو بأن كان عامله حرفا، والضمير مرفوعا إلى غير ذلك.",
     "en": "Or in that its governor is a particle and the pronoun nominative, and so on."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يريد عمدة لا دليل عليها لاستقلال ما بعدها، وإلا فالمبتدأ مع كونه عمدة يحذف.",
     "en": "He means a principal element for which there is no indication, because what follows it is independent; otherwise, the subject is omitted although it is a principal element."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: مثال الحذف الضعيف أن من يدخل الكنيسة.",
     "en": "That is, the example of the weak omission is “inna man yadkhuli al-kanīsata” (indeed, whoever enters the church)."},
    {"type": "pair",
     "ar": "وإنما جعل اسم إن ضمير الشأن؛ لأن كلمة «إن» لا يدخل على كلم المجازاة،",
     "en": "The noun of inna is taken to be the pronoun of the matter only because the word “inna” does not enter upon the words of conditional requital (kalim al-mujāzāt)."},
    {"type": "pair",
     "ar": "كتب الشارح في الحاشية: الكنيسة معبد النصارى، الجآذر جمع جؤذر، وهو ولد البقر الوحشية.",
     "en": "The Commentator wrote in the gloss: al-kanīsa is the place of worship of the Christians; al-jaʾādhir is the plural of juʾdhur, which is the calf of the wild cow."},
]
