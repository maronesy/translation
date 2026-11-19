# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 332 (printed ٣٣١)."""

PAGE_NUMBER = 332
PRINTED_PAGE = "٣٣١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «و«برجال قاعد غلمانهم»» at the foot of PDF p. 331.
    {"type": "matn",
     "ar": "مثل: «يقعد غلمانهم»، و«مررت بامرأة قائم أبوها» مثل: «يقوم أبوها» و«برجل قائمة جاريته» مثل: «تقوم جاريته»",
     "en": "…like “their slaves sit” (yaqʿudu ghilmānuhum); “I passed by a woman whose father is standing” (bi-mraʾatin qāʾimin abūhā), like “her father stands” (yaqūmu abūhā); “by a man whose slave-girl is standing” (bi-rajulin qāʾimatin jāriyatuhu), like “his slave-girl stands” (taqūmu jāriyatuhu);"},
    {"type": "matn",
     "ar": "و«برجل معمور أو معمورة داره» أو «بامرأة معمور أو معمورة دارها» مثل: «يعمر أو تعمر داره»",
     "en": "“by a man whose house is inhabited” (bi-rajulin maʿmūrin or maʿmūratin dāruhu) or “by a woman whose house is inhabited” (bi-mraʾatin maʿmūrin or maʿmūratin dāruhā), like “his house is inhabited” (yuʿmaru or tuʿmaru dāruhu);"},
    {"type": "matn",
     "ar": "و«برجل قائم أو قائمة في الدار جاريته» مثل: «يقوم أو تقوم في الدار جاريته».",
     "en": "and “by a man whose slave-girl is standing in the house” (bi-rajulin qāʾimin or qāʾimatin fī l-dāri jāriyatuhu), like “his slave-girl stands in the house” (yaqūmu or taqūmu fī l-dāri jāriyatuhu)."},
    {"type": "matn",
     "ar": "فإن قلت: إذا نظرت حق النظر[[١]] وجدت الأول -وهو الوصف بحال الموصوف- أيضا في الخمسة البواقي كالفعل؛",
     "en": "If you say: when you consider properly, you find the first—the description by a state of the qualified—also like the verb in the remaining five,"},
    {"type": "matn",
     "ar": "لأن فاعله الضمير المستكن فيه الراجع إلى موصوفه،",
     "en": "because its agent is the pronoun latent in it (al-ḍamīr al-mustakinn) referring back to its qualified noun;"},
    {"type": "matn",
     "ar": "والفعل إذا أسند إلى الضمير تلحقه الألف في التثنية، والواو في جمع المذكر العاقل، والنون في جمع المؤنث، ويؤنث في الواحدة المؤنثة،",
     "en": "and when the verb is predicated of a pronoun, the alif is attached to it in the dual, the wāw in the plural of rational masculines, and the nūn in the feminine plural, and it is put in the feminine for the single feminine."},
    {"type": "matn",
     "ar": "ولذلك قلت: «مررت برجل ضارب، وبرجلين ضاربين، وبرجال ضاربين، وبامرأة ضاربة، وبامرأتين ضاربتين، وبنسوة ضاربات»،",
     "en": "That is why you say: “I passed by a striking man, by two striking men, by striking men, by a striking woman, by two striking women, and by striking women” (ḍāribin, ḍāribayni, ḍāribīna, ḍāribatin, ḍāribatayni, ḍāribātin),"},
    {"type": "matn",
     "ar": "كما تقول في الفعل: «يضرب، ويضربان، ويضربون، وتضرب، وتضربان، ويضربن»، فلم خصصت الثاني بهذا الحكم؟",
     "en": "just as you say with the verb: “yaḍribu, yaḍribāni, yaḍribūna, taḍribu, taḍribāni, yaḍribna.” Why then did you single out the second with this rule?"},
    {"type": "matn",
     "ar": "قلنا: المقصود الأصلي في هذا المقام بيان نسبة الوصفين إلى الموصوف بالتبعية وعدمها،",
     "en": "We say: the principal aim here is to set out the relation of the two kinds of description to the qualified in terms of following (tabaʿiyya) and not following."},
    {"type": "matn",
     "ar": "ولما كان الوصف الأول يتبعه في الأمور العشرة وكان لا يخرجه مشابهته للفعل في الخمسة البواقي عن هذه التبعية، لما عرفت، اكتفى فيه بالحكم عليه بالتبعية،",
     "en": "Since the first description follows it in the ten things, and its resembling the verb in the remaining five does not take it out of this following, for the reason you have learned, he was content to rule that it follows;"},
    {"type": "matn",
     "ar": "بخلاف الوصف الثاني، فإنه لما حكم عليه بالتبعية في الخمسة الأول لم يكتف فيه بالحكم بعدم التبعية، فإنه غير مضبوط،",
     "en": "unlike the second description: having ruled that it follows in the first five, he was not content to rule that it does not follow [in the rest], since that is not determinate;"},
    {"type": "matn",
     "ar": "بل بين ضابطة عدم تبعيته له بكونه كالفعل بالنسبة إلى ظاهر بعده، ليتبين حاله عند عدم التبعية.",
     "en": "rather, he set out the rule governing its not following, namely its being like the verb in relation to an overt noun after it, so that its state when it does not follow would be made clear."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن أجل كون الوصف الثاني في الخمسة البواقي كالفعل (حسن: «قام رجل قاعد غلمانه»[[٢]]) كما حسن «يقعد غلمانه» وحسن أيضا «قاعدة غلمانه»؛",
     "en": "(Hence), that is, because the second description is like the verb in the remaining five, (“A man stood up whose slaves are sitting” (qāma rajulun qāʿidun ghilmānuhu) is good), just as “yaqʿudu ghilmānuhu” is good; and “qāʿidatun ghilmānuhu” is also good;…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه بحث؛ لأن الألف التي تلحق التثنية في الفعل نفس الفاعل والفعل مفرد كما كان، والألف التي تلحق الصفة علامة تثنيتها، والضمير مستكن.",
     "en": "This is open to discussion, because the alif attached for the dual in the verb is the agent itself, the verb remaining singular as it was; whereas the alif attached to the adjective is the sign of its being dual, and the pronoun is latent."},
    {"type": "pair",
     "ar": "وأما أن تثنيتها باعتبار تثنية فاعلها دون موصوفها فممنوع بل الأحق أنها لموصوفها،",
     "en": "That its being dual is in view of the dual of its agent rather than of its qualified noun is not conceded; rather, the sounder view is that it is for its qualified noun."},
    {"type": "pair",
     "ar": "كيف ولا يوجب تثنية الفاعل تثنية المسند بلا شبهة في موضع، ويوجب تثنية الموصوف بلا شبهة نحو: «جاءني هذان الرجلان»،",
     "en": "How could it be otherwise, when the dual of the agent does not, beyond doubt, require the dual of the predicate anywhere, while the dual of the qualified does require it beyond doubt, as in “These two men came to me”?"},
    {"type": "pair",
     "ar": "نعم يتجه على كون الوصف بحال الموصوف مطلقا تابعا للموصوف في الخمسة البواقي أيضا أنه لا يظهر في الوصف بالجملة،",
     "en": "Yes, against the description by a state of the qualified being without restriction a follower of the qualified in the remaining five as well, it may be objected that this is not apparent in description by a sentence;"},
    {"type": "pair",
     "ar": "فإن «يضربان» في «رجلان يضربان» لا يتبع رجلين، بل ألحق به ضمير الفاعل، فحصل صيغة التثنية",
     "en": "for “yaḍribāni” in “two men who strike” (rajulāni yaḍribāni) does not follow “two men”; rather, the agent pronoun was attached to it, and so the dual form resulted;"},
    {"type": "pair",
     "ar": "إلا أن يقال: أراد المتابعة حقيقة أو صورة، أو يقال: الجملة التي وقعت صفة مؤولة بمفرد مطابق.",
     "en": "unless it is said that he meant following either in reality or in form; or it is said that a sentence occurring as an adjective is interpreted as a corresponding single word."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ولو لم يكن كالفعل وكان تابعا للموصوف لوجب «قام رجل قاعد غلمانه»، وامتنع «قاعدة غلمانه».",
     "en": "Were it not like the verb but a follower of the qualified, “qāma rajulun qāʿidun ghilmānuhu” would be obligatory and “qāʿidatun ghilmānuhu” would be excluded."},
]
