# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 434 (printed ٤٣٣)."""

PAGE_NUMBER = 434
PRINTED_PAGE = "٤٣٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Begins a new paragraph after «(...إلى التاسع عشر والتاسعة عشرة).» at the foot of PDF p. 433.
    # REVIEW: a small mark (sukūn- or hamza-like) is printed over the wāw of «سواء»; written plain here.
    {"type": "matn",
     "ar": "واعلم أن حكم اسم الفاعل من العدد سواء كان بمعنى المصير أو لا حكم أسماء الفاعلين في التذكير والتأنيث،",
     "en": "Know that the rule for the active participle from a number, whether it means “that which makes” or not, is the rule of active participles in masculine and feminine gender."},
    {"type": "matn",
     "ar": "فتقول في المذكر: الثاني والثالث والرابع إلى العاشر، وتقول في المؤنث: الثانية والثالثة والرابعة إلى العاشرة،",
     "en": "So you say for the masculine: al-thānī, al-thālith, al-rābiʿ, up to al-ʿāshir; and you say for the feminine: al-thāniya, al-thālitha, al-rābiʿa, up to al-ʿāshira."},
    {"type": "matn",
     "ar": "وكذا في جميع المراتب من المركب والمعطوف نحو: الثالثة عشرة تؤنث الاسمين في المؤنث، كما تذكرهما للمذكر نحو: الثالث عشر،",
     "en": "So too in all the ranks of the compound and the conjoined, as in “al-thālithata ʿashrata” (the thirteenth, fem.): you make both nouns feminine for the feminine, just as you make them both masculine for the masculine, as in “al-thālitha ʿashara”."},
    {"type": "matn",
     "ar": "وإنما ذكروا الاسمين؛ لأنه اسم لواحد مذكر، فلا معنى للتأنيث فيه، بخلاف: ثلاثة عشر رجلا، فإنه للجماعة،",
     "en": "They made both nouns masculine only because it is a noun for a single masculine, so there is no sense in feminine marking in it; unlike “thalāthata ʿashara rajulan” (thirteen men), for that is for a group."},
    {"type": "matn",
     "ar": "وتقول في المعطوف: الثالث والعشرون والثالثة والعشرون.",
     "en": "In the conjoined you say: al-thālith wa-l-ʿishrūn (the twenty-third, masc.) and al-thālitha wa-l-ʿishrūn (fem.)."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن أجل اختلاف الاعتبارين[[١]]: اعتبار تصييره واعتبار حاله اختلف إضافتهما،",
     "en": "(Hence), that is, because of the difference between the two considerations, the consideration of its making and the consideration of its state, their annexation differs."},
    {"type": "matn",
     "ar": "فلاختلاف إضافتهما (قيل في الأول) أي: في المفرد من المتعدد المقول باعتبار تصييره (ثالث اثنين) بالإضافة[[٢]] إلى الأنقص بدرجة",
     "en": "Because their annexation differs, (it is said in the first), that is, of the single one of a multiple spoken of with regard to its making, (thālithu ithnayn) (third of two), by annexation to the number one degree less,"},
    {"type": "matn",
     "ar": "(أي: مصيرهما) أي: الاثنين، (ثلاثة من) قولهم: (ثلاثتهما) بالتخفيف أي: صيرت الاثنين ثلاثة.",
     "en": "(that is, the one making them), that is, the two, (three, from) their saying (thalathtuhumā), with the light form, that is, “I made the two three”."},
    {"type": "matn",
     "ar": "(و) قيل: (في الثاني) أي: في المفرد من المتعدد باعتبار حاله (ثالث ثلاثة) أو أربعة أو خمسة بالإضافة[[٣]] إلى عدد يساوي عدده[[٤]]، أو يكون فوقه",
     "en": "(And) it is said (in the second), that is, of the single one of a multiple with regard to its state, (thālithu thalātha) (third of three), or of four or five, by annexation to a number equal to its number, or above it,"},
    {"type": "matn",
     "ar": "(أي: أحدها) لكن لا",
     "en": "(that is, one of them); but not…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: «المستثنى» is printed (one might expect «المثنى» or similar); transcribed as printed.
    {"type": "pair",
     "ar": "الأولى أن المراد: من أجل أن الأول بمعنى ما قام به الفعل، وهو التصيير من عدد أقل إلى مرتبة العدد المستثنى هو منه بمجرد انضمامه إليه",
     "en": "It is better [to say] that what is meant is: because the first means that in which the act subsists, namely making a lesser number reach the rank of the number from which it is excepted, merely by its being joined to it;"},
    {"type": "pair",
     "ar": "أضيف إلى ما هو أقل بمرتبة، واقتصر على ما جاء الفعل فيه؛ إذ ما يؤدي معنى فعليا لا بد أن يشتق من فعل،",
     "en": "it is annexed to what is one rank less, and it is confined to cases where the verb occurs, since what conveys a verbal meaning must be derived from a verb."},
    {"type": "pair",
     "ar": "وذلك من اثنين إلى عشرة، فإنه جاء من تلك التسعة الفعل على حد ضرب بمعنى التصيير إلا فيما لامه حرف حلق، فإنه جاء فيه حد فتح أيضا،",
     "en": "That is from two to ten; for from those nine the verb occurs on the pattern of ḍaraba in the sense of making, except where the final radical is a guttural letter, for there the pattern of fataḥa also occurs."},
    {"type": "pair",
     "ar": "ولم يجيء مما دون اثنين لامتناعه عقلا، ومما فوق العشرة لامتناعه استقراء",
     "en": "It does not occur from below two, because that is rationally impossible, nor from above ten, because it is found by induction not to occur;"},
    {"type": "pair",
     "ar": "بخلاف الثاني، فإنه باعتبار حاله، وليس فيه معنى فعلي، فهو اسم فاعل صورة لا معنى،",
     "en": "unlike the second, for it is with regard to its state and there is no verbal meaning in it; so it is an active participle in form, not in meaning."},
    # REVIEW: «ف» is printed alone before «مرتبة» («واحد ف مرتبة»), evidently for «في»; transcribed as printed.
    {"type": "pair",
     "ar": "فيصح اشتقاقه من نفس العدد، ويصح إضافته إلى مثله وما فوقه؛ لأنه بمعنى واحد ف مرتبة خاصة من ذلك العدد.",
     "en": "So its derivation from the number itself is valid, and its annexation to its like and to what is above it is valid, because it means one in a particular rank of that number."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أو التنوين. والأول هنا أكثر بخلاف سائر أسماء الفاعلين، فإن الإضافة والنصب فيها متساويان، والثاني أكثر، كذا في الرضي.",
     "en": "Or the tanwīn. The first is more frequent here, unlike the other active participles, for in them annexation and the accusative are equal, and the second is more frequent. So it is in al-Raḍī."},
    {"type": "pair",
     "ar": "قال عبد الحكيم: وإذا نصب به، فإنما تنصبه إذا كان بمعنى الحال أو الاستقبال لا بمعنى الماضي",
     "en": "ʿAbd al-Ḥakīm said: when [the object] is put in the accusative by it, you put it in the accusative only when it has the sense of the present or the future, not of the past;"},
    {"type": "pair",
     "ar": "والإضافة في هذا أكثر من النصب بخلاف سائر أسماء الفاعلين، فإنهما متساويان فيها، والنصب أكثر.",
     "en": "and annexation in this is more frequent than the accusative, unlike the other active participles, for in them the two are equal, and the accusative is more frequent."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: «الجمور» is printed (for «الجمهور»); transcribed as printed.
    {"type": "pair",
     "ar": "ولا يجوز عند الجمور أن ينصب ما يضاف إليه؛ إذ ليس اسم فاعل حقيقة، ونقل الأخفش عن ثعلب جواز ذلك.",
     "en": "According to the majority, what it is annexed to may not be put in the accusative, since it is not truly an active participle; al-Akhfash reported from Thaʿlab that this is permissible."},
    {"type": "pair",
     "ar": "قال الأخفش: قلت له إذا أجزت ذلك فقد أجريته مجرى الفعل، فهل يجوز أن تقول: ثالث ثلاثة،",
     "en": "Al-Akhfash said: I said to him: if you permit that, you have treated it like the verb; so may you say “thālithun thalāthatan”?"},
    {"type": "pair",
     "ar": "قال: نعم على معنى أتممت ثلاثة، وجعلت الثلاثة ثلاثة بضم نفسي إلى اثنين.",
     "en": "He said: yes, in the sense of “I completed three, and made the three three by joining myself to two”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: العدد المأخوذ منه، فالإضافة لأدنى ملابسة.",
     "en": "That is, the number from which it is taken; so the annexation is through the slightest connection."},
    {"type": "pair",
     "ar": "ويجب أن يقول: بالإضافة إلى عدده؛ لأن الاثنين بعينه عدد أخذ منه الثاني لا مثل ذلك العدد.",
     "en": "He should have said “by annexation to its number”, because ithnān itself is the number from which al-thānī is taken, not something like that number."},
]
