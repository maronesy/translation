# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 595 (printed ٥٩٤)."""

PAGE_NUMBER = 595
PRINTED_PAGE = "٥٩٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows the verse «أقلي اللوم عاذل والعتابن …» at the foot of PDF p. 594.
    {"type": "matn",
     "ar": "فروي هذا البيت الباء، وحصل بإشباع فتحها الألف، وعوض عن الألف عند التغني نون التنوين.",
     "en": "The rhyme letter (rawī) of this verse is the bāʾ; through the lengthening of its fatḥa an alif arose, and in singing the nūn of the tanwīn was given in compensation for the alif."},
    {"type": "matn",
     "ar": "وإما أن يلحق القافية المقيدة، وهي ما كان رويها حرفا ساكنا صحيحا كان أو غير صحيح،",
     "en": "Or it attaches to the restricted rhyme (al-qāfiya al-muqayyada), which is one whose rhyme letter is a quiescent letter, whether sound or not sound."},
    {"type": "matn",
     "ar": "وسميت مقيدة لتقييد الصوت بها وامتناع الامتداد؛ لأنه ليس هناك حركة يحصل من إشباعها حرف الإطلاق؛ ليتيسر امتداد الصوت بها كقول الشاعر:",
     "en": "It is called restricted because the voice is restrained by it and prolongation is barred; for there is no vowel there from whose lengthening a letter of release would arise, so that prolonging the voice with it would be easy; as in the poet's words:"},
    {"type": "verse",
     "ar": "وقاتم الأعماق خاوي المخترقن          مشتبه الأعلام لماع الخفقن",
     "en": "And many a dark-depthed, empty-tracked [desert], its waymarks confusing, flashing with mirage —"},
    # REVIEW: printed «روى» (with alif maqṣūra), where «روي» is expected; transcribed as printed.
    {"type": "matn",
     "ar": "فإن روى القافية في هذا البيت القاف الساكنة، ولا يمكن مد الصوت بها، فحركت عند التغني بالفتح أو الكسر وألحق بها النون، فقيل: «المخترقن، والخفقن»،",
     "en": "For the rhyme letter of the rhyme in this verse is the quiescent qāf, and the voice cannot be prolonged with it; so in singing it was given a fatḥa or a kasra and the nūn was attached to it, and one said “al-mukhtaraqan” and “al-khafaqan”."},
    # REVIEW: printed «التجاوز عند الحد» where «عن الحد» is expected; transcribed as printed, translated by the sense.
    {"type": "matn",
     "ar": "ويسمى هذا القسم من التنوين «الغالي»؛ لأن الغلو هو التجاوز عند الحد، وقد تجاوز البيت بلحوق هذا التنوين عن حد الوزن،",
     "en": "This kind of tanwīn is called “al-ghālī” (the excessive), because excess (ghuluww) is going beyond the limit, and the verse goes beyond the limit of the metre by the attaching of this tanwīn;"},
    # REVIEW: printed «يسقط عد التقطيع», where «عند التقطيع» is expected (or «عد» = counting); transcribed as printed.
    {"type": "matn",
     "ar": "ولهذا يسقط عد التقطيع، وليس للقسم الأول اسم يختص به.",
     "en": "for this reason it drops out in scansion (taqṭīʿ). The first kind has no name proper to it."},
    # REVIEW: printed «لأن معناه الترنم» (because its meaning is chanting), which contradicts the
    # sentence; the sense requires «لا أن معناه الترنم» (not that its meaning is chanting). Transcribed and translated as printed.
    {"type": "matn",
     "ar": "واعلم أن تنوين الترنم ليس موضوعا بإزاء معنى من المعاني، بل هو موضوع لغرض الترنم؛ لأن معناه الترنم،",
     "en": "Know that the tanwīn of chanting is not assigned (mawḍūʿ) to correspond to any meaning; rather it is assigned for the purpose of chanting, because its meaning is chanting [sic],"},
    {"type": "matn",
     "ar": "كما أن حرف التهجي موضوع لغرض التركيب، لا بإزاء معنى من المعاني،",
     "en": "just as a letter of the alphabet (ḥarf al-tahajjī) is assigned for the purpose of composition, not to correspond to any meaning."},
    {"type": "matn",
     "ar": "ففي عده تنوين الترنم من أقسام الحروف، التي هي من أقسام الكلمة المعتبرة فيها الوضع تساهل وتسامح.",
     "en": "So in his counting the tanwīn of chanting among the kinds of particles — which are among the kinds of the word (kalima), in which assignment (waḍʿ) is a condition — there is laxity and leniency."},
    {"type": "matn",
     "ar": "وأما التنوينات الأخر، ففي اعتبار الوضع في بعضها أيضا تأمل.",
     "en": "As for the other kinds of tanwīn, the consideration of assignment in some of them also calls for reflection."},
    {"type": "matn",
     "ar": "(ويحذف) أي: التنوين (وجوبا من العلم) حال كونه (موصوفا بابن) حال كون الابن (مضافا إلى علم آخر) نحو: «جاءني زيد بن عمرو»،",
     "en": "(And it is elided), that is, the tanwīn, (obligatorily from the proper name) when it is (qualified by “ibn”), the “ibn” being (annexed to another proper name), as in “jāʾanī Zaydu bnu ʿAmrin” (Zayd son of ʿAmr came to me)."},
    {"type": "matn",
     "ar": "وذلك لكثرة استعمال «ابن» بين علمين أحدهما موصوف به، والآخر مضاف إليه له،",
     "en": "That is because of the frequent use of “ibn” between two proper names, one of them qualified by it and the other the second term of its annexation;"},
    {"type": "matn",
     "ar": "فطلب التخفيف لفظا بحذف التنوين من موصوفه، وخطا بحذف ألف «ابن»،",
     "en": "so lightening was sought in pronunciation by eliding the tanwīn from what it qualifies, and in writing by eliding the alif of “ibn”."},
    {"type": "matn",
     "ar": "وكذلك قولهم: «هذا فلان بن فلان»؛ لأنه كناية عن العلم.",
     "en": "Likewise their saying “hādhā fulānu bnu fulānin” (this is so-and-so son of so-and-so), because it is a metonym for the proper name."},
    {"type": "matn",
     "ar": "ويعلم منه أنه إذا كان صفة لغير العلم، أو كان مضافا إلى غير العلم، نحو: «جاءني رجل ابن زيد، وزيد ابن عالم»، لم يحذف التنوين من اللفظ، وألف «ابن» من الخط، لقلة الاستعمال",
     "en": "It is understood from this that if it qualifies something other than a proper name, or is annexed to something other than a proper name, as in “jāʾanī rajulun ibnu Zaydin” (a man, son of Zayd, came to me) and “Zaydun ibnu ʿālimin” (Zayd, son of a scholar), the tanwīn is not elided from pronunciation, nor the alif of “ibn” from writing, because of infrequent use."},
    {"type": "matn",
     "ar": "ويعلم من قوله: «موصوفا» أنه لا يحذف إذا لم يكن الابن صفة نحو: «زيد ابن عمرو» على أن يكون «ابن عمرو» خبرا عن «زيد».",
     "en": "And it is understood from his word “qualified” that it is not elided when “ibn” is not an attribute, as in “Zaydun ibnu ʿAmrin” (Zayd is the son of ʿAmr), with “ibnu ʿAmrin” the predicate of “Zayd”."},
    {"type": "matn",
     "ar": "وحكم «الابنة» حكم «الابن» في جميع ما ذكرنا، إلا في حذف همزتها، فإنها لا تحذف حيثما كانت، لئلا تلتبس بـ«بنت» في مثل: «هذه هند ابنة عاصم».",
     "en": "The rule for “ibna” (daughter) is the rule for “ibn” in all that we have mentioned, except for the elision of its hamza: it is not elided wherever it occurs, lest it be confused with “bint”, as in “hādhihi Hindu bnatu ʿĀṣimin” (this is Hind daughter of ʿĀṣim)."},
]
